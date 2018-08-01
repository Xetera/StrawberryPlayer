import pytest
from ..utils.packet import stringify


def test_stringify():
    test_obj = {
        'key': 'value',
        'key2': 'value2'
    }
    assert stringify(test_obj) == '{"key": "value", "key2": "value2"}'