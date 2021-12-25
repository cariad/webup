from pytest import mark

from webup import set_content_type
from webup.content_type import content_type

set_content_type("jpeg3000", "image/jpeg3000")
set_content_type("JPEG4000", "image/jpeg4000")


@mark.parametrize(
    "suffix, expect",
    [
        ("css", "text/css"),
        (".css", "text/css"),
        ("CSS", "text/css"),
        (".CSS", "text/css"),
        ("eot", "application/vnd.m-fontobject"),
        ("html", "text/html"),
        ("jpeg3000", "image/jpeg3000"),
        ("jpeg4000", "image/jpeg4000"),
        ("js", "text/javascript"),
        ("png", "image/png"),
        ("ttf", "font/ttf"),
        ("woff", "font/woff"),
        ("woff2", "font/woff2"),
    ],
)
def test_content_type(suffix: str, expect: str) -> None:
    assert content_type(suffix) == expect
