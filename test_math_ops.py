import pytest
from pytest_mock import mocker
import math_ops
from datetime import date


def test_number_add(mocker):
    obj = math_ops.MathOps()

    obj.calc.add = mocker.MagicMock(return_value=8, spec=math_ops.Calculator)

    assert obj.number_add(3,5) == 8
    obj.calc.add.assert_called_with(3, 5)


class datetime_date_patch:
    @classmethod
    def date(cls):
        return date(2020, 5, 22)
    
    @classmethod
    def timedelta(cls):
        return date(2020, 5, 24)

@pytest.fixture
def patch_datetime(monkeypatch):
    monkeypatch.setattr(math_ops.datetime, "datetime", datetime_date_patch)

def test_date_add(mocker, patch_datetime):
    obj = math_ops.MathOps()

    assert obj.date_add(math_ops.datetime.date(2020, 5, 21), 2) == str(date(2020, 5, 23))
    
