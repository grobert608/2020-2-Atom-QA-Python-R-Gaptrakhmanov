import pytest


def test_copy(random_dict_non_empty):
    copy_list = random_dict_non_empty.copy()
    assert copy_list == random_dict_non_empty


def test_clear(random_dict_non_empty):
    random_dict_non_empty.clear()
    assert len(random_dict_non_empty) == 0


def test_pop(random_dict_non_empty):
    len_dict = len(random_dict_non_empty)
    random_dict_non_empty.popitem()
    # что-то удалидось
    assert len_dict == len(random_dict_non_empty) + 1


class TestDict:

    @pytest.mark.parametrize("dict_for_testing, expected",
                             [({1: 1, 2: 2, 3: 3}, [1, 2, 3]), ({1: 'one', 2: 'two'}, ['one', 'two']), ({}, [])])
    def test_values_with_parametrization(self, dict_for_testing, expected):
        assert list(dict_for_testing.values()) == expected

    def test_keys(self):
        dict_init = {'key0': 0, 'key1': 1, 'key2': 2}
        dict_keys = ['key0', 'key1', 'key2']
        assert list(dict_init.keys()) == dict_keys
