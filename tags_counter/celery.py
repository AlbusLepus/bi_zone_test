"""
Celery app module
"""
from celery import Celery

# rabbit login can be changed and password can be added,
# I just didn't setup it in my system
# pylint: disable=C0103
app = Celery("tag_tasks")
app.config_from_object("tags_counter.celeryconfig")
