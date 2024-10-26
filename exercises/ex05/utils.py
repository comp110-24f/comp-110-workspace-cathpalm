"""Creating more list utils"""

__author__ = "730625616"


def only_evens(input: list[int]) -> list[int]:
    """Returns a new list with only the even values"""
    evens = []
    for elem in input:
        # even
        if elem % 2 == 0:
            evens.append(elem)
    return evens


def sub(input: list[int], start: int, end: int) -> list[int]:
    """Returns a new list that is a subset of the input list"""
    subset = []
    if len(input) == 0 or start >= len(input) or end <= 0:
        return subset
    if start < -1:
        start = 0
    if end > len(input):
        end = len(input)
    for idx in range(start, end):
        subset.append(input[idx])
    return subset


def add_at_index(input: list[int], value: int, insert: int) -> None:
    """Mutates the list by inserting a value at a specified index"""
    if insert < 0 or insert > len(input):
        raise IndexError("Index is out of bounds for the input list")
    idx = len(input)
    # need a placeholder so that the values can be shifted
    input.append(0)
    while idx > insert:
        input[idx] = input[idx - 1]
        idx = idx - 1
    input[insert] = value
