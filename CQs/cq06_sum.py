"""Summing the elements of a list using different loops"""

__author__ = "730756130"


def w_sum(values: list[float]) -> float:
    index: int = 0
    w_sum: float = 0
    while index <= len(values) - 1:
        # iterates through values and adds the value at each index to sum variable
        w_sum += values[index]
        index += 1
    return w_sum


def f_sum(f_values: list[float]) -> float:
    f_sum: float = 0
    for value in f_values:
        # uses the for loop to check each value in f_values
        f_sum += value
    return f_sum


def f_range_sum(range_values: list[float]) -> float:
    range_sum: float = 0
    for idx in range(0, len(range_values)):
        # creates index that goes through by 1 all the way to the end of the list but does not include that value
        range_sum += range_values[idx]
    return range_sum
