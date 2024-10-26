"""Making functinos to test"""


def get_first(input: list[str]) -> str:
    """Returns frist element"""
    return input[0]


def remove_first(input: list[str]) -> None:
    """Pops first element off the list"""
    input.pop(0)


def get_and_remove_first(input: list[str]) -> str:
    """Returns first element and removes it"""
    first: str = input[0]
    input.pop(0)
    return first
