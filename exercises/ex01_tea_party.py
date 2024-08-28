"""Helpful program for planning a tea party!!!"""

__author__ = "730625616"


def main_planner(guests: int) -> None:
    """Entrypoint of the program"""

    """Use tea_bags and treats in cost arguments"""
    """Make everything strings and print the final display of the information"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Determines how many tea bags needed"""
    return int(people * 2)


def treats(people: int) -> int:
    """Determines the number of treats needed"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Determines the total cost for the party"""
    return float(tea_count * 0.5 + treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests? ")))
