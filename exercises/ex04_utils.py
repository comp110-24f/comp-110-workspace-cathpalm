"""Understanding utilities of lists"""

__author__ = "730625616"


def all(list_: list[int], num: int) -> bool:
    """Checks if all the numbers in the list are the same as the number inputted"""
    index = 0
    if len(list_) == 0:
        return False
    while index < len(list_):
        if list_[index] != num:
            return False
        index += 1
    # this will only be reached if num is equal to all the numbers in the list
    return True


def max(list_: list[int]) -> int:
    """Returns the maximum value in the list"""
    if len(list_) == 0:
        raise ValueError("max() arg is an empty list")
    index: int = 0
    max_num = list_[index]
    while index < len(list_):
        # updates the max_num if the next number checked is greater
        if list_[index] > max_num:
            max_num = list_[index]
        index += 1
    return max_num


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Checks if two lists are exactly equal"""
    if len(list_1) != len(list_2):
        return False
    index = 0
    while index < len(list_1):
        if list_1[index] != list_2[index]:
            return False
        index += 1
    # this return is only reached if we exit the loop
    return True


def extend(list_1: list[int], list_2: list[int]) -> None:
    """Appends the contents of list 2 to list 1"""
    for elem in list_2:
        list_1.append(elem)
