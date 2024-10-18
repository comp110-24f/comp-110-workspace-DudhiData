"""Exercise 05 List Utility Functions"""

__author__ = "730756130"


def only_evens(input: list[int]) -> list[int]:
    even_input: list[int] = []
    # creates list that will hold subset of integers
    for value in input:
        # goes through each value in input list
        if value % 2 == 0:
            # checks to see if each value is even and adds them to the even list
            even_input.append(value)
    return even_input


def sub(input_2: list[int], start_index: int, end_index: int) -> list[int]:
    sub_input_2: list[int] = []
    # creates list that will hold subset of original list
    if len(input_2) == 0:
        return sub_input_2
        # measure for when empty list given, returns empty list
    if start_index < 0:
        start_index = 0
        # if start_index is less than 0 it changes the value of start_index to 0
    if end_index > len(input_2):
        end_index = len(input_2)
        # if end_index is greater than the length of the list, it changes end_index to the last index
    while start_index < end_index:
        sub_input_2.append(input_2[start_index])
        # goes from start_index to end_index and appends each value at those indices to subset list
        # start_index should be always less than end_index since we are not including end_index's value
        start_index += 1
    return sub_input_2


def add_at_index(input_3: list[int], add_value: int, value_index: int) -> None:
    if value_index < 0 or value_index > len(input_3):
        raise IndexError("Index is out of bounds for the input list")
        # measure to check whether the value_index is too low or high for the list, raises IndexError if so
    input_3.append(0)
    # adds placeholder value to the end of the list that we can replace during shifting
    index: int = len(input_3) - 1
    # initializes index at the last value of the list
    while index != value_index:
        # keeps dropping index until it gets to the index value where we want to put add_value
        input_3[index] = input_3[index - 1]
        # replaces the value at the current index with the value before it
        index -= 1
    input_3[value_index] = add_value
    # once we get to value_index, it replaces the value at that index with add_value since the previous value has been shifted to the right
