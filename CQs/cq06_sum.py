"""Summing the elements of a list using different loops"""

__author__ = "730625616"


def w_sum(vals: list[float]) -> float:
    """Sums the values in the list with a while loop"""
    index = 0
    sum = 0
    while index < len(vals):
        sum += vals[index]
        index += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Sums the values of the list with a for in loop"""
    sum = 0
    for num in vals:
        sum += num
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Sums the values of the list with a for in range() loop"""
    sum = 0
    for idx in range(len(vals)):
        sum += vals[idx]
    return sum
