"""Making a function to be tested"""

__author__ = "730625616"


def find_and_remove_max(input: list[int]) -> int:
    if len(input) == 0:
        return -1
    index: int = 0
    max_num = input[index]
    while index < len(input):
        # updates the max_num if the next number checked is greater
        if input[index] > max_num:
            max_num = input[index]
        index += 1
    # new variable to keep track of index
    idx = 0
    while idx < len(input):
        if input[idx] == max_num:
            input.pop(idx)
        else:  # need the else statement because the index shifts if .pop is used
            idx += 1
    return max_num
