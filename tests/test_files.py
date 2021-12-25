from pathlib import Path

from webup.files import Files
from webup.models import File


def test_next() -> None:
    walkable = Path(".") / "tests" / "walkable"
    files = Files(walkable)

    for _ in range(4):
        file = files.next
        assert file in [
            File(key="index.html", path=walkable / "index.html"),
            File(key="style.css", path=walkable / "style.css"),
            File(key="images/image.jpg", path=walkable / "images" / "image.jpg"),
            File(key="images/image.png", path=walkable / "images" / "image.png"),
        ]

    assert files.next is None


def test_max_path() -> None:
    walkable = Path(".") / "tests" / "walkable"
    files = Files(walkable)

    expect_path = walkable / "images" / "image.png"
    expect = len(expect_path.as_posix())
    assert files.max_path == expect
