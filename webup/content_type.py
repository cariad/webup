from typing import Dict

from webup.suffix import normalize_suffix

_content_types: Dict[str, str] = {}

default_content_type = "application/octet-stream"
"""
Default content type.
"""


def content_type(suffix: str) -> str:
    """
    Gets the Content-Type header for a type of file.

    Arguments:
        suffix: Filename suffix.
    """

    suffix = normalize_suffix(suffix)
    return _content_types.get(suffix, default_content_type)


def register_content_type(suffix: str, content_type: str) -> None:
    """
    Registers the content type of a type of file.

    Arguments:
        suffix: Filename suffix.
    """

    suffix = normalize_suffix(suffix)
    _content_types[suffix] = content_type


register_content_type("css", "text/css")
register_content_type("eot", "application/vnd.m-fontobject")
register_content_type("html", "text/html")
register_content_type("js", "text/javascript")
register_content_type("png", "image/png")
register_content_type("ttf", "font/ttf")
register_content_type("woff", "font/woff")
register_content_type("woff2", "font/woff2")
