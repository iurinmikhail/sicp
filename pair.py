"""Модуль реализации пар."""
from typing import Callable, Sequence
from _types import Numer, Denom, DenomEnd, ListPair, Pair, TypeSelectorEnum, Index


def cons(n: Numer, d: Denom | Pair | ListPair) -> Pair | ListPair:
    """Конструктор для создания пары."""
    def rat(t: TypeSelectorEnum) -> Numer | Denom:
        match t:
            case TypeSelectorEnum.NUMER:
                return n
            case TypeSelectorEnum.DENOM:
                return d
    return rat


def car(x: Pair | ListPair) -> Numer:
    """Получить числитель"""
    return x(TypeSelectorEnum.NUMER)


def cdr(x: Pair | ListPair) -> Denom | DenomEnd:
    """Получить знаменатель."""
    return x(TypeSelectorEnum.DENOM)


def list_(l: Sequence[int]) -> ListPair:
    """Создает список пар."""
    if not l:
        return None
    return cons(l[0], list_(l[1:]))


def is_pair_end(items: ListPair) -> bool:
    """Проверяет, последние ли это элемент в списке пар."""
    return cdr(items) is None


def map_(func: Callable, items: ListPair) -> ListPair:
    """Преобразует список применяя функцию к значению пары."""
    if is_none(items):
        return None
    return cons(func(car(items)), map_(func, cdr(items)))

def append(items1: ListPair, items2: ListPair) -> ListPair:
    """Создает новый объединенный список."""
    if is_none(items1):
        return items2
    return cons(car(items1), append(cdr(items1), items2))


def len_(items: ListPair) -> int:
    """Возвращает количество элементов в списке пар."""
    def len_iter(a: ListPair, count: int):
        if is_none(a):
            return count
        return len_iter(cdr(a), count + 1)
    return len_iter(items, 0)


def list_ref(conses: ListPair, num: Index) -> Numer:
    if num == 0:
        return car(conses)
    return list_ref(cdr(conses), num - 1)

def is_pair(x: None | int | ListPair | Pair) -> bool:
    return callable(x)


def scale_list(items: ListPair, factor: int) -> ListPair:
    """Какая выражен здесь моя мысль. Примени к каждому значенияю функию lambda x: x * factor и выведи получившийся
    список пар"""
    return map_(lambda x: x * factor, items)

def is_none(x: None | int | ListPair | Pair) -> bool:
    return x is None

def is_equal(items1: ListPair, items2: ListPair) -> bool:
    """Проверка, что списки пар равны."""
    return is_equal_tree(items1, items2)


def is_equal_tree(items1: ListPair, items2: ListPair) -> bool:
    """Проверка, что списки пар равны."""
    if is_none(items1) and is_none(items2):
        return True
    if is_none(items1) or is_none(items2):
        return False

    if not is_pair(items1) and not is_pair(items2):
        return items1 == items2

    return is_equal_tree(cdr(items1), cdr(items2)) and is_equal_tree(car(items1), car(items2))


def scale_tree(tree: ListPair, factor: int) -> ListPair:
    return map_(
        lambda sub_tree: scale_tree(sub_tree, factor) if is_pair(sub_tree) else sub_tree * factor,
        tree,
    )

def square(x: int) -> int:
    """Возводит в квадрат."""
    return x * x


def is_odd(x: int) -> bool:
    """Проверяет, является ли число нечетным."""
    return x % 2 != 0


def is_even(x: int):
    """Проверяет, является ли число четным."""
    return x % 2  == 0
