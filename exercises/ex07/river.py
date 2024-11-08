"""File to define River class."""

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear

__author__ = "730756130"


class River:
    """Class definition for River object."""

    day: int
    fish: list[Fish]
    bears: list[Bear]
    """Declares day, fish, bears attributes."""

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        """Initializes day as 0 and the fish and bears attributes as empty lists."""
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Declare a placeholder list that will hold Fish objects that have an age of 3 or less."""
        survive_fish: list[Fish] = []
        for fish in self.fish:
            # goes through each Fish object and checks their age
            if fish.age <= 3:
                survive_fish.append(fish)
                # populates placeholder list
        self.fish = survive_fish
        # copies placeholder to normal fish list
        """Declare a placeholder list that will hold Bear objects that have an age of 5 or less."""
        survive_bear: list[Bear] = []
        for bear in self.bears:
            # goes through each Bear object and checks age
            if bear.age <= 5:
                survive_bear.append(bear)
                # populates placeholder list
        self.bears = survive_bear
        # copies placeholder to normal bear list
        return None

    def bears_eating(self):
        """Bears eat fish and lessen their hunger."""
        for bear in self.bears:
            # goes through each Bear object
            if len(self.fish) >= 5:
                # if the fish population is at least 5 the bear can eat
                self.remove_fish(3)
                # the bear eats and 3 fish die
                bear.eat(3)
                # the bear increases hunger score
        return None

    def check_hunger(self):
        """Removes starving bears."""
        fittest_bears: list[Bear] = []
        # creates placeholder list that will hold eligible bears
        for bear in self.bears:
            # goes through each Bear object
            if bear.hunger_score != 0:
                # if the hunger is not 0 then add them to placeholder
                fittest_bears.append(bear)
        self.bears = fittest_bears
        # copies placeholder to normal bear list

        return None

    def repopulate_fish(self):
        """Fish mate and add to the population."""
        new_fish: int = (len(self.fish) // 2) * 4
        # this will hold the number of eggs that will be made
        idx: int = 0
        while idx < new_fish:
            # repeats the number of eggs and adds a Fish object each time
            self.fish.append(Fish())
            idx += 1
        return None

    def repopulate_bears(self):
        """Bears mate and add to the population."""
        new_bears: int = (len(self.bears)) // 2
        # this will hold the number of cubs that will be made
        idx: int = 0
        while idx < new_bears:
            self.bears.append(Bear())
            # repeats the number of cubs and adds a Bear object each time
            idx += 1
        return None

    def view_river(self):
        """Visualizes the day and bear/fish populations."""
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
        """Repeats the river day method 7 times."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()

    def remove_fish(self, amount: int):
        """Removes three fish from the front."""
        leftover_fish: list[Fish] = []
        # placeholder list declared
        for i in range(amount, len(self.fish)):
            # iterates through subsection of list that will not be removed and adds them to new list
            leftover_fish.append(self.fish[i])
        self.fish = leftover_fish
        # copies placeholder list to normal fish list
        return None
