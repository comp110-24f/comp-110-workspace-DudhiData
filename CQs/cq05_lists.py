"""Mutating Functions."""

__author__ = "730756130"


def manual_append(mutate_list: list[int], append_int: int) -> None:
    mutate_list.append(append_int)
    # adds append_int to the end of the list that we want to mutate through the use .append


def double(double_list: list[int]) -> None:
    index: int = 0
    # initializes index we will use to iterate through list
    while index <= len(double_list) - 1:
        double_list[index] *= 2
        # takes the number at that index and doubles it
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = [1, 2, 3]
# creating two lists with two different ID numbers in the heap, meaning that mutating list_2 won't affect list_1
double(list_2)
print(list_1)
print(list_2)
