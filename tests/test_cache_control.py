from pytest import mark

from webup import set_default_maximum_age, set_maximum_age
from webup.cache_control import cache_control

set_default_maximum_age(99)
set_maximum_age("css", 10)
set_maximum_age("PNG", 20)


@mark.parametrize(
    "suffix, expect",
    [
        ("css", "max-age=10"),
        (".css", "max-age=10"),
        ("CSS", "max-age=10"),
        (".CSS", "max-age=10"),
        ("png", "max-age=20"),
        ("foo", "max-age=99"),
    ],
)
def test_cache_control(suffix: str, expect: str) -> None:
    assert cache_control(suffix) == expect
