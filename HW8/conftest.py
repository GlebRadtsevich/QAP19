import random
from pytest import fixture

@fixture
def random_list():
    random_numbers = random.sample(range(0, 100), 10)
    return random_numbers

a