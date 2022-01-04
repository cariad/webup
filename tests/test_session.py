from mock import patch
from mock.mock import Mock

from webup.session import make_session


def test_make_session() -> None:
    mocked = Mock()
    with patch("webup.session.Session", return_value=mocked) as session_cls:
        actual = make_session("eu-east-17")

    session_cls.assert_called_once_with(region_name="eu-east-17")
    assert actual is mocked


def test_make_session__default() -> None:
    mocked = Mock()
    with patch("webup.session.Session", return_value=mocked) as session_cls:
        actual = make_session()

    session_cls.assert_called_once_with()
    assert actual is mocked
