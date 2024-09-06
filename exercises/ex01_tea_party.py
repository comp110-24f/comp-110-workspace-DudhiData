"""Planning a cozy tea party!"""

__author__ = "730756130"


def main_planner(people: int) -> None:
    """Calls each function and produces final output (entrypoint of program)"""
    """Make sure to turn int and float types to str to concatenate to the rest of the string."""
    print("A Cozy Tea Party for " + str(people) + " People!")
    print("Tea Bags: " + str(tea_bags(people)))
    print("Treats: " + str(treats(people)))
    print("Cost: $" + str(cost(tea_count=tea_bags(people), treat_count=treats(people))))
    """Really confused on how to create values for tea_count and treat_count, decided to assign them values during paramter stage"""


def tea_bags(people: int) -> int:
    """Calculating the # of tea bags needed (2 per person, so multiply by 2)"""
    return people * 2


def treats(people: int) -> int:
    """Calculating # of treats needed based on the # of teas expected to be drank (in this case, 1.5 treats per tea)"""
    """Since we take the output from tea_bags we don't need to multiply by 3 here, just multiply by 1.5"""
    """Keyword argument allows for the value for people from the tea bags function to be sent to the treats function"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculating the cost of the tea bags and the treats combined!"""
    """Have to define tea_count and treat_count at some point"""
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    """Only works when all functions are able to be ran, that's why it's at the bottom"""
    main_planner(people=int(input("How many guests are attending your tea party?")))
