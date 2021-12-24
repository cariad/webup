from mock import Mock
from pytest import fixture


@fixture
def client(put_object: Mock) -> Mock:
    s3 = Mock()
    s3.put_object = put_object

    return Mock(return_value=s3)


@fixture
def put() -> Mock:
    return Mock()


@fixture
def put_object() -> Mock:
    return Mock()


@fixture
def queue(put: Mock) -> Mock:
    queue = Mock()
    queue.put = put
    return queue


@fixture
def session(client: Mock) -> Mock:
    session = Mock()
    session.client = client
    return session
