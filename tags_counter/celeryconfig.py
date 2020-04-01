"""
Celery configs.
"""
# pylint: disable=C0114
# pylint: disable=C0103
## Broker settings.
broker_url = "pyamqp://guest@localhost:5672//"

# List of modules to import when the Celery worker starts.
# pylint: disable=C0103
imports = ("tags_counter.tasks",)

## Using the database to store task state and results.
# pylint: disable=C0103
result_backend = "redis://:123@localhost:6379/0"
