from io import StringIO
from logging import getLogger
from multiprocessing import Queue
from pathlib import Path

from mock import patch
from mock.mock import Mock
from pytest import mark, raises

from webup import upload
from webup.models import Output, UploadResult
from webup.queue import bucket_name, check

getLogger("webup").setLevel("DEBUG")
walkable = Path(".") / "tests" / "walkable"


def test_bucket_name__bucket() -> None:
    assert bucket_name("foo", None, None) == "foo"


def test_bucket_name__none() -> None:
    with raises(ValueError):
        bucket_name(None, None, None)


def test_bucket_name__ssm(session: Mock) -> None:
    with patch("webup.queue.get_ssm_value", return_value="bar") as get_ssm_value:
        with patch("webup.queue.make_session", return_value=session) as make_session:
            actual = bucket_name(None, "foo", "eu-east-17")

    make_session.assert_called_once_with("eu-east-17")
    get_ssm_value.assert_called_once_with("foo", session)
    assert actual == "bar"


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
    with patch("webup.session.Session"):
        upload(
            bucket="buck",
            concurrent_uploads=2,
            dir=dir,
            region="eu-east-17",
        )
