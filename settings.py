"""
Settings-module for Tags Counter project.
"""
from tags_counter.utils import get_required_env_var

REDIS_CONNECTION = {
    "host": "localhost",
    "port": 6379,
    "db": 10,  # not 0 just in case
    "password": get_required_env_var("REDIS_PASSWORD"),
}