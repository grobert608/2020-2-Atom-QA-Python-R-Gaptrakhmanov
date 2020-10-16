import random
import pytest
import string


@pytest.fixture()
def random_list_non_empty():
    yield random.sample(range(1, 1000), random.randint(5, 15))


@pytest.fixture()
def random_set_non_empty():
    yield set(random.sample(range(1, 1000), random.randint(5, 15)))


@pytest.fixture()
def random_dict_non_empty():
    yield {'key' + str(a): a for a in range(random.randrange(5, 15))}


@pytest.fixture()
def random_string_non_empty():
    yield ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(5, 15)))


@pytest.fixture()
def random_positive_int():
    yield random.randint(1, 1000)
