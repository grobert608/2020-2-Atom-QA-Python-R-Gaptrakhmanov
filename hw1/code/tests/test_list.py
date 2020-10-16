import random
import pytest


def test_copy(random_list_non_empty):
    copy_list = random_list_non_empty.copy()
    assert copy_list == random_list_non_empty


def test_append(random_list_non_empty, random_positive_int):
    copy_list = random_list_non_empty.copy()
    copy_list.append(random_positive_int)
    # проверяем, что добавилось
    assert len(copy_list) == len(random_list_non_empty) + 1
    # проверяем, что последний элемент - добавленный
    assert copy_list[len(random_list_non_empty)] == random_positive_int


def test_clear(random_list_non_empty):
    random_list_non_empty.clear()
    assert len(random_list_non_empty) == 0


def test_pop(random_list_non_empty):
    copy_list = random_list_non_empty.copy()
    i = random.randint(0, len(random_list_non_empty) - 1)
    deleted = copy_list.pop(i)
    # проверяем, что удалили
    assert len(copy_list) == len(random_list_non_empty) - 1
    # проверяем, что удаленный элемент - нужный
    assert deleted == random_list_non_empty[i]


@pytest.mark.parametrize("list_for_testing, expected",
                         [([1, 2, 3, 4], [1, 2, 3, 4]), ([4, 3, 2, 1], [1, 2, 3, 4])])
def test_sort_with_parametrization(list_for_testing, expected):
    list_for_testing.sort()
    assert list_for_testing == expected


class TestList:

    def test_reverse(self):
        list_init = [1, 2, 3, 4, 5]
        list_rev = [5, 4, 3, 2, 1]
        list_init.reverse()
        assert list_rev == list_init
