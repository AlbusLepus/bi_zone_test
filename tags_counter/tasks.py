"""
Celery tasks module.
"""
from requests.exceptions import RequestException

from tags_counter.celery import app
from tags_counter.processing import handle_html_url


@app.task(throws=RequestException)
def handle_tags_in_page_task(url: str):
    """
    Celery task to handle url
    :param url:
    :return:
    """
    return handle_html_url(url)
