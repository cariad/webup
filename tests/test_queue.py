from logging import getLogger
from multiprocessing import Queue
from pathlib import Path

from mock import patch
from pytest import mark, raises

from webup import upload
from webup.models import UploadResult
from webup.queue import check_for_done

getLogger("webup").setLevel("DEBUG")
walkable = Path(".") / "tests" / "walkable"


def test_check_for_done() -> None:
    queue: "Queue[UploadResult]" = Queue(1)
    queue.put(UploadResult(bucket="buck", path=__file__, key="foo.bar"))

    wip = ["foo.bar"]

    check_for_done(queue=queue, timeout=2, wip=wip)

    assert not wip


def test_check_for_done__empty() -> None:
    queue: "Queue[UploadResult]" = Queue(1)
    wip = ["foo.bar"]

    check_for_done(queue=queue, timeout=2, wip=wip)

    assert wip == ["foo.bar"]


def test_check_for_done__exception() -> None:
    queue: "Queue[UploadResult]" = Queue(1)
    queue.put(
        UploadResult(
            bucket="buck",
            path=__file__,
            key="foo.bar",
            exception=Exception("fire"),
        )
    )

    wip = ["foo.bar"]

    with raises(Exception) as ex:
        check_for_done(queue=queue, timeout=2, wip=wip)

    assert not wip
    assert str(ex.value) == "fire"


@mark.parametrize("dir", [(walkable), (walkable.as_posix())])
def test_upload(dir: str | Path) -> None:
    # We can't query the session because it's in another thread, but we can
    # patch it to prevent any real AWS API calls.
    with patch("webup.upload_process.Session"):
        result = upload(
            bucket="buck",
            concurrent_uploads=2,
            dir=dir,
            region="eu-east-17",
        )

    assert result.process_count == 4
