from logging import getLogger

from mock import ANY, Mock, patch

from webup.models import UploadResult
from webup.upload_process import Upload

getLogger("webup").setLevel("DEBUG")


def test_run(put: Mock, queue: Mock) -> None:
    with patch("webup.upload_process.Session"):
        Upload(
            bucket="buck",
            cache_control="max-age=600",
            content_type="foo/bar",
            key="foo.bar",
            path=__file__,
            queue=queue,
            read_only=False,
            region="eu-east-17",
        ).run()

    put.assert_called_once_with(
        UploadResult(
            bucket="buck",
            key="foo.bar",
            path=__file__,
        )
    )


def test_run__fail(put: Mock, queue: Mock) -> None:
    exception = Exception("fire")

    with patch("webup.upload_process.Session", side_effect=exception):
        Upload(
            bucket="buck",
            cache_control="max-age=600",
            content_type="foo/bar",
            key="foo.bar",
            path=__file__,
            queue=queue,
            read_only=False,
            region="eu-east-17",
        ).run()

    put.assert_called_once_with(
        UploadResult(
            bucket="buck",
            exception=exception,
            key="foo.bar",
            path=__file__,
        )
    )


def test_try_upload(client: Mock, put_object: Mock, session: Mock) -> None:
    with patch("webup.upload_process.Session", return_value=session):
        Upload(
            bucket="buck",
            cache_control="max-age=600",
            content_type="foo/bar",
            key="foo.bar",
            path=__file__,
            queue=Mock(),
            read_only=False,
            region="eu-east-17",
        ).run()

    client.assert_called_once_with("s3")

    put_object.assert_called_once_with(
        Body=ANY,
        Bucket="buck",
        CacheControl="max-age=600",
        ContentType="foo/bar",
        Key="foo.bar",
    )


def test_try_upload__read_only(client: Mock, put_object: Mock, session: Mock) -> None:
    with patch("webup.upload_process.Session", return_value=session):
        Upload(
            bucket="buck",
            cache_control="max-age=600",
            content_type="foo/bar",
            key="foo.bar",
            path=__file__,
            queue=Mock(),
            read_only=True,
            region="eu-east-17",
        ).run()

    client.assert_called_once_with("s3")
    put_object.assert_not_called()
