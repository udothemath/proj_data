from the_variables import TheVariables, input_abc
import pytest
from pytest import MonkeyPatch


def test_larger_value():
    a = TheVariables(234, -999)
    assert a.larger_than_100 > 100


def test_invalid_input_value():
    a = TheVariables(17, -999)
    with pytest.raises(ValueError):
        a.check_input_value(5)


def test_input_abc(monkeypatch: MonkeyPatch):
    inputs = [3, 4, 5]
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
    input_abc()
