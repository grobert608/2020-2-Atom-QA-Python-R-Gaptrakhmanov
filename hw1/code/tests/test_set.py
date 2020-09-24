import pytest


def test_copy(random_set_non_empty):
    copy_list = random_set_non_empty.copy()
    assert copy_list == random_set_non_empty


def test_clear(random_set_non_empty):
    random_set_non_empty.clear()
    assert len(random_set_non_empty) == 0


def test_pop(random_set_non_empty):
    len_set = len(random_set_non_empty)
    random_set_non_empty.pop()
    # что-то удалидось
    assert len_set == len(random_set_non_empty) + 1


def test_add(random_set_non_empty, random_positive_int):
    if random_positive_int in random_set_non_empty:
        len_set = len(random_set_non_empty)
        random_set_non_empty.add(random_positive_int)
        assert len_set == len(random_set_non_empty)
    else:
        len_set = len(random_set_non_empty)
        random_set_non_empty.add(random_positive_int)
        assert len_set == len(random_set_non_empty) - 1
        assert random_positive_int in random_set_non_empty


@pytest.mark.parametrize("other_set, expected, create_set",
                         [({9, 10, 11}, {9}, {i for i in range(10)}), ({10, 11}, set(), {i for i in range(10)}),
                          (set(), set(), {i for i in range(10)})])
def test_intersection_with_parametrization(other_set, expected, create_set):
    set_for_testing = create_set
    assert set_for_testing.intersection(other_set) == expected


class TestSet:

    def test_update(self):
        set_first = {1, 2, 3, 4, 5}
        set_second = {5, 6, 7, 8, 8}
        set_result = {1, 2, 3, 4, 5, 6, 7, 8, 8}
        set_first.update(set_second)
        assert set_first == set_result
