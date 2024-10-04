"""Mutating functions."""

__author__ = "730625616"


def manual_append(list: list[int], new: int) -> None:
    list.append(new)


def double(list: list[int]) -> None:
    index = 0
    while index < len(list):
        list[index] = list[index] * 2
        index += 1
