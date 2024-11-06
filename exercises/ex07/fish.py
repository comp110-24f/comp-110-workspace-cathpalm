"""File to define Fish class."""

__author__ = "730625616"


class Fish:
    """Fish object simulates the activities of fish in the river."""

    age: int

    def __init__(self):
        """Creates a new Fish."""
        self.age = 0
        return None

    def one_day(self):
        """Updates the age of a Fish object after one simulated day."""
        self.age += 1
        return None
