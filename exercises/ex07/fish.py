"""File to define Fish class."""

__author__ = "730756130"


class Fish:
    """Class definition for Fish type."""

    age: int
    """Declares age attribute."""

    def __init__(self):
        """Constructs Fish object with age attribute of 0 when called."""
        self.age = 0
        return None

    def one_day(self):
        """Method specific to Fish object that adds 1 to age when called."""
        self.age += 1
        return None
