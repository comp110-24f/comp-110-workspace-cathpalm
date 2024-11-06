"""File to define Bear class."""

__author__ = "730625616"


class Bear:
    """Bear object simulates the activities of bears in the river."""

    age: int
    hunger_score: int

    def __init__(self):
        """Creates a new Bear."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Updates attributes of a Bear object after one simluated day."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Simulates a Bear eating by updating its hunger score."""
        self.hunger_score += num_fish
