from pathlib import Path

from webup.files import Files
from webup.models import File


def test() -> None:
    walkable = Path(".") / "tests" / "walkable"
    files = Files(walkable)

    for _ in range(4):
        file = files.next
        assert file in [
            File(key="1.txt", path=walkable / "1.txt"),
            File(key="2.txt", path=walkable / "2.txt"),
            File(key="sub/1.txt", path=walkable / "sub" / "1.txt"),
            File(key="sub/2.txt", path=walkable / "sub" / "2.txt"),
        ]

    assert files.next is None
