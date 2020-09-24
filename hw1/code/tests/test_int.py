import pytest


def test_abs(random_positive_int):
    assert abs(-random_positive_int) == random_positive_int


def test_zero_division(random_positive_int):
    with pytest.raises(ZeroDivisionError):
        random_positive_int / 0


def test_2pow(random_positive_int):
    assert pow(random_positive_int, 2) == random_positive_int ** 2


class TestInt:

    @pytest.mark.parametrize("test_input_f,test_input_s,expected", [(3, 5, 8), (2, 4, 6), (30, 12, 42)])
    def test_sum_with_parametrization(self, test_input_f, test_input_s, expected):
        assert test_input_f + test_input_s == expected

    @pytest.mark.parametrize("test_input_f,test_input_s,expected", [(3, 5, -2), (2, 4, -2), (30, 12, 18)])
    def test_sub_with_parametrization(self, test_input_f, test_input_s, expected):
        assert test_input_f - test_input_s == expected
