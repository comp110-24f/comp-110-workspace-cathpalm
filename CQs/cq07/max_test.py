"""Testing find_and_remove_max"""

__author__ = "730625616"

from find_max import find_and_remove_max


def test_max_value() -> None:
    """Tests the return value for a typical usage"""
    a: list[int] = [1, 2, 4, 3, 4]
    assert find_and_remove_max(a) == 4


def test_list() -> None:
    """Tests the mutated list"""
    a: list[int] = [10, 23, 14, 15, 23, 16, 10, 3, 4]
    find_and_remove_max(a)
    assert a == [10, 14, 15, 16, 10, 3, 4]


def test_edge() -> None:
    """Tests an edge case"""
    a: list[int] = []
    assert find_and_remove_max(a) == -1
