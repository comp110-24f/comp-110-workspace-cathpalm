"""Testing more list utils"""

__author__ = "730625616"

import pytest
from exercises.ex05.utils import only_evens, sub, add_at_index


def test_only_evens_return() -> None:
    """Testing that a use case returns the correct value"""
    a = [1, 2, 3, 4, 6, 5]
    assert only_evens(a) == [2, 4, 6]


def test_only_evens_edge() -> None:
    """Testing an edge case where there are no even values"""
    b = [3, 5, 79, 241]
    assert only_evens(b) == []


def test_only_evens_mutate() -> None:
    """Tests that the function does not mutate the input"""
    c = [1, 2, 3, 4]
    only_evens(c)
    assert c == [1, 2, 3, 4]


def test_sub_return() -> None:
    """Tests that a use case returns the expected value"""
    a = [1, 2, 3, 4, 5]
    assert sub(a, 0, 2) == [1, 2]


def test_sub_edge() -> None:
    """Tests an edge case where start and end values are outside range of indices"""
    a = [2, 24, 3, 46, 5]
    assert sub(a, -2, 7) == [2, 24, 3, 46, 5]


def test_sub_mutate() -> None:
    """Tests that the funciton does not mutate the input"""
    a = [3, 4, 5, 5, 7]
    sub(a, 3, 4)
    assert a == [3, 4, 5, 5, 7]


def test_add_at_index_mutate() -> None:
    """Tests that the function properly mutates the input list"""
    a = [1, 2, 3, 4, 5]
    add_at_index(a, 6, 1)
    assert a == [1, 6, 2, 3, 4, 5]


def test_add_at_index_return() -> None:
    """Tests that the function does not have a return value"""
    a = [1, 2, 3]
    assert add_at_index(a, 2, 1) is None


def test_add_at_index_indexerror() -> None:
    """Test that the function raises an IndexError when index is out of range"""
    a = [2, 34, 56, 3]
    with pytest.raises(IndexError):
        add_at_index(a, 10, 5)
