"""Testing the functions"""

from list_fns import get_first
from list_fns import remove_first


def test_get_first() -> None:
    assert get_first(["a", "b", "c"]) == "a"


def test_remove_first() -> None:
    TAs: list[str] = ["V", "S", "B"]
    remove_first(TAs)
    assert TAs == ["S", "B"]
