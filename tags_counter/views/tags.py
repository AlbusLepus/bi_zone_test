"""
Module contains views for handling html-tags.
It would be better (TODO) to implement swagger-docstring in methods
"""
import json

from celery.result import AsyncResult

from tags_counter.tasks import app
from tags_counter.views import EasyRejectableRequestHandler
from tags_counter import tasks


# pylint: disable=W0223
class TagsHandler(EasyRejectableRequestHandler):
    """
    View-class, contains post method that takes url-address.
    """
    def post(self):
        """
        POST API-method requires url inside the body of the request,
        launch task to handle the page.
        :return: id of the task.
        """
        self.set_header("Content-Type", "application/json")
        url = json.loads(self.request.body).get("url")
        if not url:
            self.error_response(
                error_message="Url is required inside the request body: "
                              "{'url': url}"
            )

        res = tasks.handle_tags_in_page_task.delay(url)
        self.write({"id": res.id})


# pylint: disable=W0223
class TagsResultHandler(EasyRejectableRequestHandler):
    """
    View-class, contains get method that takes task-id.
    """
    def get(self, task_id: str):
        """
        GET API-method gets the result of the task.
        :param task_id: uuid
        :return: dict of counted html tags from the page
        or error message if the task failed
        """
        task_result = AsyncResult(task_id, app=app)
        if task_result.state in ["STARTED", "PENDING", "RETRY"]:
            self.write(
                f"Task with id {task_id} is still in process,"
                f" status: {task_result.status}"
            )
        else:
            counted_tags = None
            error_message = None
            status_code = 200
            if task_result.state == "FAILURE":
                error_message = "Task failed"
                status_code = 400
            else:
                task_data = task_result.get()

                if task_data.get("error_message"):
                    error_message = task_data["error_message"]
                    status_code = task_data.get("status", 400)
                else:
                    counted_tags = task_data.get("counted_tags")

            if error_message:
                self.error_response(status=status_code,
                                    error_message=error_message)

            self.write(counted_tags)
