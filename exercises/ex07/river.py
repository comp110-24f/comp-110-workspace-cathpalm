"""File to define River class."""

__author__ = "730625616"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """River object simulates the interactions of bears and fish."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Updates lists of bears and fish based on age."""
        surviv_fish: list[Fish] = []
        # adding surviving fish to a new list
        for fish in self.fish:
            if fish.age <= 3:
                surviv_fish.append(fish)
        # updates initial list to be equal to the new one
        self.fish = surviv_fish

        surviv_bears: list[Bear] = []
        # adding surviving bears to a new list
        for bear in self.bears:
            if bear.age <= 5:
                surviv_bears.append(bear)
        # updates initial list to be equal to the new one
        self.bears = surviv_bears
        return None

    def remove_fish(self, amount: int):
        """Removes specified number of fish from the front of self.fish."""
        for idx in range(0, amount):
            self.fish.pop(idx)

    def bears_eating(self):
        """Simulates a bear eating."""
        for bear in self.bears:
            if len(self.fish) > 5:
                bear.eat(3)
                self.remove_fish(3)
        return None

    def check_hunger(self):
        """Removes bears with hunger scores <0."""
        surviv_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                surviv_bears.append(bear)
        self.bears = surviv_bears
        return None

    def repopulate_fish(self):
        """Adds new fish with every two initial fish producing 4 offspring."""
        new_fish = (len(self.fish) // 2) * 4
        for _ in range(0, new_fish):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Adds new bears with every two initial bears prodicing 2 offspring."""
        new_bears = len(self.bears) // 2
        for _ in range(0, new_bears):
            self.bears.append(Bear())
        return None

    def view_river(self):
        """Displays the status of the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulates one week of life in the river."""
        for _ in range(0, 7):
            self.one_river_day()
        return None
