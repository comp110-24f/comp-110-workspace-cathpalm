from __future__ import annotations


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


def recursive_range(start: int, end: int) -> Node | None:
    if start > end:
        raise ValueError("Start value is greater than end, try again!")
    if start == end:
        return None
    else:
        first: int = start
        rest: Node | None = recursive_range(start + 1, end)
        return Node(first, rest)
