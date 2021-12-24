from pytest import mark

from webup import cache_control, default_max_age, register_max_age

register_max_age("css", 10)
register_max_age("PNG", 20)


@mark.parametrize(
    "suffix, expect",
    [
        ("css", "max-age=10"),
        (".css", "max-age=10"),
        ("CSS", "max-age=10"),
        (".CSS", "max-age=10"),
        ("png", "max-age=20"),
        ("foo", "max-age=60"),
    ],
)
def test_cache_control(suffix: str, expect: str) -> None:
    assert cache_control(suffix) == expect


def test_default_max_age() -> None:
    assert default_max_age == 60
