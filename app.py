"""
The main run-script for Tags Counter project.
"""
from tornado.web import Application
from tornado.ioloop import IOLoop

from tags_counter.views import TagsHandler, TagsResultHandler


def make_app():
    urls = [
        ("/tags/", TagsHandler),
        ("/tags/(.*)", TagsResultHandler),
    ]
    return Application(urls, debug=True)


if __name__ == "__main__":
    # pylint: disable=C0103
    app = make_app()
    app.listen(3000)
    IOLoop.instance().start()
