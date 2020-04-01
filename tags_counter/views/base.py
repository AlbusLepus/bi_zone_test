"""
Module contains view that implements base functional for other views
of the project.
"""
from tornado.web import RequestHandler, Finish


# pylint: disable=W0223
class EasyRejectableRequestHandler(RequestHandler):
    """
    View-class that implements base functional for all other views
    """
    def error_response(self, status: int = 400, error_message: str = None):
        """
        Method which responds with error information.
        :param status: status code of the http-error
        :param error_message: message of the error
        :return:
        """
        if isinstance(status, int):
            status = 400
        self.set_status(status, reason=error_message)
        if error_message is None:
            error_message = "Unkown error"
        self.finish(error_message)
        raise Finish
