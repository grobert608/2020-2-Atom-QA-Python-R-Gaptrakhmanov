import pytest


def test_islower(random_string_non_empty):
    assert random_string_non_empty.islower()


def test_startswith(random_string_non_empty):
    first = random_string_non_empty[0]
    assert random_string_non_empty.startswith(first)


def test_isalpha(random_string_non_empty):
    assert random_string_non_empty.isalpha()


def test_isdigit(random_string_non_empty):
    assert not random_string_non_empty.isdigit()


@pytest.mark.parametrize("string_for_testing, expected", [("", 0), ("abc", 3)])
def test_len_with_parametrization(string_for_testing, expected):
    assert len(string_for_testing) == expected


class TestString:

    def test_plus(self):
        str_first = "qwe"
        str_second = "rty"
        str_result = "qwerty"
        assert str_first + str_second == str_result
