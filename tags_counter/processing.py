"""
Main logic for html-page tags handling.
"""
import requests
from requests.exceptions import RequestException
from lxml import html

from tags_counter.utils import count_elems


def handle_html_url(url: str) -> dict:
    """
    Method counts every tag from the html page.
    :param url: url-address of html page to handle
    :return: dict with url and (dict with counted html tags or error message)
    """
    try:
        page = requests.get(url)
    except RequestException:
        return {
            "url": url,
            "error_message": f"Could not get from url {url}."
        }

    return handle_html_page(url, page.content)


def handle_html_page(url, page) -> dict:
    result = {"url": url}
    tree = html.fromstring(page)

    if tree.find(".//*") is None:
        result["error_message"] = f"Url {url} does not contain any html-page."
        return result

    all_tags = [item.tag for item in tree.xpath("//*")]
    counted_tags = count_elems(all_tags)
    result["counted_tags"] = counted_tags
    print(result)
    return result
