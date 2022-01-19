from pathlib import Path

from pytest import mark

from webup import set_default_maximum_age, set_maximum_age
from webup.cache_control import cache_control

set_default_maximum_age(99)
set_maximum_age(r"^sw\.js$", 0)
set_maximum_age(r"^.*\.js$", 10)
set_maximum_age(r"^.*\.png$", 20)


@mark.parametrize(
    "path, expect",
    [
        (Path("sw.js"), "max-age=0"),
        (Path("index.js"), "max-age=10"),
        (Path("logo.png"), "max-age=20"),
        (Path("logo.js.png"), "max-age=20"),
        (Path("styles.css"), "max-age=99"),
    ],
)
def test_cache_control(path: Path, expect: str) -> None:
    assert cache_control(path) == expect
