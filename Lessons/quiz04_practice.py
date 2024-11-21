from __future__ import annotations


def sum_of_natural_numbers(n: int) -> int:
    if n == 0:
        return 0
    else:
        sum_start: int = n
        sum_rest: int = sum_of_natural_numbers(n - 1)
        return sum_start + sum_rest


def power(num: int, val: int) -> int:
    if val == 0:
        return 1
    else:
        return num * power(num, val - 1)


def gcd(num_1: int, num_2: int) -> int:
    if num_1 > num_2:
        a = num_1
        b = num_2
    else:
        a = num_2
        b = num_1

    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def reverse_string(s: str) -> str:
    return reverse_helper(s=s, index=len(s) - 1)


def reverse_helper(s: str, index: int) -> str:
    if index < 0:
        return ""
    else:
        start = s[index]
        rest = reverse_helper(s, index - 1)
        return start + rest


def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_sequence(up_to: int, fib_list: list[int]) -> list[int]:
    if len(fib_list) < 2:
        fib_list = [0, 1]
    next = fib_list[len(fib_list) - 1] + fib_list[len(fib_list) - 2]
    if next > up_to:
        return fib_list
    else:
        fib_list.append(next)
        return fibonacci_sequence(up_to, fib_list)


def binary_search(arr: list[int], target: int, low: int, high: int) -> int:
    if low > high:
        return -1

    search_index = (low + high) // 2

    if arr[search_index] == target:
        return search_index
    elif target < arr[search_index]:
        high = search_index - 1
    else:
        low = search_index + 1

    return binary_search(arr, target, low, high)
