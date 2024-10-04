"""EX04: List Utility Functions"""

__author__ = "730756130"


def all(test_list: list[int], test_int: int) -> bool:
    index: int = 0
    count: int = 0
    if len(test_list) == 0:
        # checks to see if list is empty, and if it is, returns False
        return False
    while index <= len(test_list) - 1:
        # repeats through list
        if test_int == test_list[index]:
            count += 1
        # checks to see whether the integer parameter is equal to any index of the list and counts how many times this occurs
        index += 1
    if count == len(test_list):
        # if all values are equal to the integer parameter then the count variable, that checks the number of equalities, should be equal to the length of the list
        return True
    else:
        return False


def max(max_list: list[int]) -> int:
    if len(max_list) == 0:
        raise ValueError("max() arg is an empty list")
    # raises ValueError if empty list entered
    index: int = 0
    max_value: int = max_list[0]
    # initializes max value with the first value in the list
    while index < len(max_list) - 1:
        if max_value < max_list[index + 1]:
            # checks to see whether the current max value is less than the next value in the list
            max_value = max_list[index + 1]
            # changes max value to the next largest value
        index += 1
    return max_value


def is_equal(deep_list1: list[int], deep_list2: list[int]) -> bool:
    index: int = 0
    count: int = 0
    if len(deep_list1) != len(deep_list2):
        return False
    # ensures that the length of both lists are equal
    while index <= len(deep_list1) - 1:
        # since we checked for inequal list lengths, we can use deep_list1 or deep_list2
        if deep_list1[index] == deep_list2[index]:
            count += 1
            # checks to see whether the values at the same index in both lists are equal
            # if they're equal, then the count variable increases to track the number of equalities
        index += 1
    if count == len(deep_list1):
        # if the number of equalities is equal to the length of the list, that means all values in the lists match at each index
        return True
    else:
        return False


def extend(original_list: list[int], append_list: list[int]) -> None:
    index: int = 0
    while index <= len(append_list) - 1:
        # iterates through append_list and takes the value at each index and appends it to original_list
        original_list.append(append_list[index])
        index += 1
