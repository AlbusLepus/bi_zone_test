"""
Tests for tags_counter.processing module.
"""
from tags_counter.processing import handle_html_page, handle_html_url


def test_handle_html_page_simple_success():
    """ handle_html_page test1 """
    url = "http://test.url"
    page = """
    <html>
      <head>
        <title>test</title>
      </head>
      <body>
        <h1>test</h1>
        <h1>test</h1>
      </body>
    </html>
    """
    expected = {
        "counted_tags": {
            "html": 1, "head": 1, "title": 1, "body": 1, "h1": 2
        },
        "url": "http://test.url"
    }
    assert handle_html_page(url, page) == expected


def test_handle_html_page_simple_fail():
    """ handle_html_page test2 """
    url = "http://test.url"
    page = "simple string"
    expected = {
        "error_message": "Url http://test.url does not contain any html-page.",
        "url": "http://test.url"
    }
    assert handle_html_page(url, page) == expected


def test_handle_html_url_success():
    """ handle_html_url test1 """
    url = "http://facebook.com"
    result = handle_html_url(url)
    # not asserting the exact dict because who knows
    assert len(result) == 2
    assert result["url"] == url
    assert result.get("error_message") is None
    assert result.get("counted_tags") is not None
    assert result["counted_tags"].get("html") is not None
    assert isinstance(result["counted_tags"]["html"], int)


def test_handle_html_url_simple_fail():
    """ handle_html_url test2 """
    url = "http://test.test"
    expected = {
        "error_message": f"Could not get from url http://test.test.",
        "url": "http://test.test"
    }
    assert handle_html_url(url) == expected
