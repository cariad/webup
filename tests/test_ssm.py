from mock import Mock
from pytest import raises

from webup.ssm import get_ssm_value


def test_get_ssm_value() -> None:
    get_parameter = Mock(return_value={"Parameter": {"Value": "bar"}})

    ssm = Mock()
    ssm.get_parameter = get_parameter

    client = Mock(return_value=ssm)

    session = Mock()
    session.client = client

    actual = get_ssm_value("foo", session)

    client.assert_called_once_with("ssm")
    get_parameter.assert_called_once_with(Name="foo")
    assert actual == "bar"


def test_get_ssm_value__incomplete_response() -> None:
    get_parameter = Mock(return_value={})

    ssm = Mock()
    ssm.get_parameter = get_parameter

    client = Mock(return_value=ssm)

    session = Mock()
    session.client = client

    with raises(KeyError):
        get_ssm_value("foo", session)

    client.assert_called_once_with("ssm")
    get_parameter.assert_called_once_with(Name="foo")
