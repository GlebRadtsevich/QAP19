from pytest import mark


class Test1:
    @mark.len
    def test_len(self):
        assert len([1, 2, 3]) == 3
        assert len("") == 0
        assert len("hello") == 5

    @mark.sum
    def test_sum(self):
        assert sum([1, 2, 3]) == 6
        assert sum([]) == 0
        assert sum([-1, -2, -3]) == -6

    @mark.sorted
    def test_sorted(self):
        assert sorted([3, 1, 2]) == [1, 2, 3]
        assert sorted([]) == []
        assert sorted([5, 5, 5]) == [5, 5, 5]


@mark.skip
def test_even(random_list):
    for i in random_list:
        assert i % 2 == 0

@mark.xfail
def test_odd(random_list):
    for i in random_list:
        assert i % 2 != 0
