"""Creating and practicing with the Node class."""

from __future__ import annotations

__author__ = "730625616"


class Node:
    """Node class creates a linked list."""

    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        """Creates a Node object."""
        self.value = val
        self.next = next

    def __str__(self) -> str:
        """Prints a description of the linked list."""
        rest: str = ""
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


def to_str(head: Node | None) -> str:
    """Returns a string form of a linked list."""
    # Base case
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


def last(head: Node) -> int:
    """Returns the last value in a linked list."""
    # Base case
    if head.next is None:
        return head.value
    else:
        return last(head.next)


def value_at(head: Node | None, index: int) -> int:
    """Returns the value at a specified index in a linked list."""
    if head is None:
        raise IndexError("Index if out of bounds in list.")
    if index == 0:
        return head.value
    # Including index - 1 moves us closer to the base case of index being 0
    else:
        return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Returns maximum value in a linked list."""
    if head is None:
        raise ValueError("Cannot call max with None")
    # Base case
    if head.next is None:
        return head.value
    max_val = max(head.next)
    # Compares and updates the maximum value
    if head.value > max_val:
        return head.value
    else:
        return max_val


def linkify(items: list[int]) -> Node | None:
    """Creates a linked list from a list of integers."""
    # Accounts for case of empty list
    if items == []:
        return None
    # Initializes the first Node
    head = Node(items[0], None)
    head.next = linkify(items[1:])
    return head


def scale(head: Node | None, factor: int) -> Node | None:
    """Creates a new linked list from the inputed one with values multipied by a specified factor."""
    # Base case
    if head is None:
        return None
    new_head = Node(head.value * factor, None)
    new_head.next = scale(head.next, factor)
    return new_head
