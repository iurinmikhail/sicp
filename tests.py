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
    is_none,
    is_equal_tree,
    scale_tree,
    )

def test_cons():
    """Тест на согласовоность данных (консистентность)"""
    r = cons(1, 2)
    assert car(r) == 1
    assert cdr(r) == 2

def test_map_():
    items = list_([1, 2, 3, 4])
    expected = list_([10, 20, 30, 40])
    func = lambda x: x * 10
    result = map_(func, items)
    assert is_equal_tree(result, expected)

def test_is_equal():
    r1 = list_([1, 2, 3])
    r2 = list_([1, 2, 3])
    r3 = list_([2, 3, 4])
    r4 = list_([1, 3, 4])
    assert is_equal_tree(r1, r2)
    assert not is_equal_tree(r1, r3)
    assert not is_equal_tree(r1, r4)

def test_append():
    r = list_([1, 2, 3])
    r2 = list_([100, 200, 300])
    expected = list_([1, 2, 3] + [100, 200, 300])
    assert is_equal(append(r, r2), expected)


def test_len_():
    r = list_([1, 2, 3])
    assert len_(r) == 3


def test_list_ref():
    """Функция по индексу получает значение в числителе пары."""
    squares = list_([x*x for x in range(10)])
    assert list_ref(squares, 0) == 0
    assert list_ref(squares, 4) == 16


def test_is_pair_end():
    pairs_to_expected = (
        (cons(1, None), True),
        (cons(1, 2), False),
        (cons(cons(1, None), cons(2, None)), False),
        )
    for pair, exp in pairs_to_expected:
        assert is_pair_end(pair) == exp


def test_is_pair():
    elements_to_expected = (
        (cons(1, 2), True),
        (1, False),
        (cons(cons(1, None), cons(2, None)), True),
        (None, False),
    )
    for elem, exp in elements_to_expected:
        assert is_pair(elem) == exp


def test_is_equal_tree():
    items = list_([1, list_([2, list_([3, 4]), 5]), list_([6, 7])])
    expected = list_([1, list_([2, list_([3, 4]), 5]), list_([6, 7])])
    expected_fail = list_([1, list_([2, list_([30, 4]), 5]), list_([6, 7])])
    assert is_equal_tree(items, expected)
    assert not is_equal_tree(items, expected_fail)


def test_is_equal_tree__when_simple_list():
    items = list_([1, 2, 3])
    expected = list_([1, 2, 3])
    expected_fail = list_([0, 1, 2, 3])
    assert is_equal_tree(items, expected)
    assert not is_equal_tree(items, expected_fail)


def test_scale_list():
    items = list_([1, 2, 3, 4])
    expected = list_([10, 20, 30, 40])
    factor = 10
    result = scale_list(items, factor)
    assert is_equal_tree(result, expected)


def test_scale_tree():
    items = list_([1, list_([2, list_([3, 4]), 5]), list_([6, 7])])
    expected = list_([10, list_([20, list_([30, 40]), 50]), list_([60, 70])])
    factor = 10
    result = scale_tree(items, factor)
    assert is_equal_tree(result, expected)

if __name__ == "__main__":
    test_cons()
    test_map_()
    test_is_equal()
    test_append()
    test_len_()
    test_list_ref()
    test_is_pair_end()
    test_is_pair()
    test_is_equal_tree()
    test_is_equal_tree__when_simple_list()
    test_scale_list()
    test_scale_tree()
