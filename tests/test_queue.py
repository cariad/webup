from io import StringIO
from logging import getLogger
from multiprocessing import Queue
from pathlib import Path

from mock import patch
from pytest import mark, raises

from webup import upload
from webup.models import Output, UploadResult
from webup.queue import check

getLogger("webup").setLevel("DEBUG")
walkable = Path(".") / "tests" / "walkable"


def test_check() -> None:
    queue: "Queue[UploadResult]" = Queue(1)
    queue.put(UploadResult(bucket="buck", path=__file__, key="foo.bar"))

    wip = ["foo.bar"]

    check(queue=queue, timeout=2, wip=wip)

    assert not wip


def test_check__empty() -> None:
    queue: "Queue[UploadResult]" = Queue(1)
    wip = ["foo.bar"]

    check(queue=queue, timeout=2, wip=wip)

    assert wip == ["foo.bar"]


def test_check__exception() -> None:
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
        check(queue=queue, timeout=2, wip=wip)

    assert not wip
    assert str(ex.value) == "fire"


def test_check__output() -> None:
    queue: "Queue[UploadResult]" = Queue(1)
    queue.put(UploadResult(bucket="buck", path="./foo.bar", key="foo.bar"))

    wip = ["foo.bar"]

    out = StringIO()
    output = Output(max_path=10, out=out)

    check(output=output, queue=queue, timeout=2, wip=wip)

    assert not wip
    assert out.getvalue() == "./foo.bar  ~> s3:/buck/foo.bar\n"


@mark.parametrize("dir", [(walkable), (walkable.as_posix())])
def test_upload(dir: str | Path) -> None:
    # We can't query the session because it's in another thread, but we can
    # patch it to prevent any real AWS API calls.
    with patch("webup.upload_process.Session"):
        upload(
            bucket="buck",
            concurrent_uploads=2,
            dir=dir,
            region="eu-east-17",
        )
