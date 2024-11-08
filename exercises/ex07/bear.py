"""File to define Bear class."""

__author__ = "730756130"


class Bear:
    """Bear class definition."""

    age: int
    hunger_score: int
    """Declaring age and hunger attributes for bear class."""

    def __init__(self):
        """Constructs an instance of the Bear object."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Adds 1 to age and subtracts 1 from hunger for each day when called, specific to Bear class."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Adds the # of fish removed to hunger."""
        self.hunger_score += num_fish
        return None
