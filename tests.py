import unittest

from pair import (
    cons,
    car,
    cdr,
    list_,
    map_,
    is_equal,
    is_pair_end,
    append,
    len_,
    list_ref,
    is_pair,
    scale_list,
    is_equal_tree,
    scale_tree,
    to_list,
)


class TestPair(unittest.TestCase):

    def test_cons(self):
        """Тест на согласовоность данных (консистентность)"""
        r = cons(1, 2)
        assert car(r) == 1
        assert cdr(r) == 2

    def test_map_(self):
        items = list_([1, 2, 3, 4])
        expected = list_([10, 20, 30, 40])
        func = lambda x: x * 10
        result = map_(func, items)
        assert is_equal_tree(result, expected)

    def test_is_equal(self):
        r1 = list_([1, 2, 3])
        r2 = list_([1, 2, 3])
        r3 = list_([2, 3, 4])
        r4 = list_([1, 3, 4])
        assert is_equal_tree(r1, r2)
        assert not is_equal_tree(r1, r3)
        assert not is_equal_tree(r1, r4)

    def test_append(self):
        r = list_([1, 2, 3])
        r2 = list_([100, 200, 300])
        expected = list_([1, 2, 3] + [100, 200, 300])
        assert is_equal(append(r, r2), expected)

    def test_len_(self):
        r = list_([1, 2, 3])
        assert len_(r) == 3

    def test_list_ref(self):
        """Функция по индексу получает значение в числителе пары."""
        squares = list_([x * x for x in range(10)])
        assert list_ref(squares, 0) == 0
        assert list_ref(squares, 4) == 16

    def test_is_pair_end(self):
        pairs_to_expected = (
            (cons(1, None), True),
            (cons(1, 2), False),
            (cons(cons(1, None), cons(2, None)), False),
        )
        for pair, exp in pairs_to_expected:
            assert is_pair_end(pair) == exp

    def test_is_pair(self):
        elements_to_expected = (
            (cons(1, 2), True),
            (1, False),
            (cons(cons(1, None), cons(2, None)), True),
            (None, False),
        )
        for elem, exp in elements_to_expected:
            assert is_pair(elem) == exp

    def test_is_equal_tree(self):
        items = list_([1, list_([2, list_([3, 4]), 5]), list_([6, 7])])
        expected = list_([1, list_([2, list_([3, 4]), 5]), list_([6, 7])])
        expected_fail = list_([1, list_([2, list_([30, 4]), 5]), list_([6, 7])])
        assert is_equal_tree(items, expected)
        assert not is_equal_tree(items, expected_fail)

    def test_is_equal_tree__when_simple_list(self):
        items = list_([1, 2, 3])
        expected = list_([1, 2, 3])
        expected_fail = list_([0, 1, 2, 3])
        assert is_equal_tree(items, expected)
        assert not is_equal_tree(items, expected_fail)

    def test_scale_list(self):
        items = list_([1, 2, 3, 4])
        expected = list_([10, 20, 30, 40])
        factor = 10
        result = scale_list(items, factor)
        assert is_equal_tree(result, expected)

    def test_scale_tree(self):
        items = list_([1, list_([2, list_([3, 4]), 5]), list_([6, 7])])
        expected = list_([10, list_([20, list_([30, 40]), 50]), list_([60, 70])])
        factor = 10
        result = scale_tree(items, factor)
        assert is_equal_tree(result, expected)

    def test_to_list(self):
        l = [1, 2, [3, [4, 1]]]
        l_pair = list_(l)
        assert to_list(l_pair) == l


if __name__ == "__main__":
    unittest.main()
