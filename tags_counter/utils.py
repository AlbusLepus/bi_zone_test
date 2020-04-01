"""
Module contains helpful utils-functions.
"""
import os


def get_required_env_var(name: str) -> str:
    """
    :param name: name of the environment variable
    :return: value of the environment variable
    """
    val = os.getenv(name)
    if val is None:
        raise ValueError("enviroment variable {} is not set".format(name))
    return val


def count_elems(repetitive_items: list) -> dict:
    """
    :param repetitive_items: list of some items
    :return: dict with the amount of each unique item in list
    """
    counter = {}
    for item in repetitive_items:
        if item not in counter:
            counter[item] = 1
        else:
            counter[item] += 1
    return counter
