from pathlib import Path

from webup.files import Files
from webup.models import File


def test() -> None:
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
