from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest

# imports wanted functions and pytest for IndexError check
"""Exercise 05 Testing List Utility Functions"""

__author__ = "730756130"


def test_return_only_evens() -> None:
    input: list[int] = [1, 3, 5, 2, 3, 8, 11, 5]
    # checks to see whether the function returns a subset of integers
    # containing only the even integers from the initial list
    assert only_evens(input) == [2, 8]


def test_mutate_only_evens() -> None:
    input: list[int] = [1, 3, 5, 2, 3, 8, 11, 5]
    only_evens(input)
    # checks to see whether the initial list is not mutated after the function is ran
    assert input == [1, 3, 5, 2, 3, 8, 11, 5]


def test_empty_or_odd_only_evens() -> None:
    input: list[int] = []
    input_1: list[int] = [1, 3, 5, 3, 11, 5]
    # checks to see if the function returns empty lists when the input lists are either empty or full of only odd numbers
    assert (only_evens(input) == []) and (only_evens(input_1) == [])


def test_return_sub() -> None:
    input: list[int] = [1, 2, 3, 4, 5]
    start_index: int = 2
    end_index: int = 4
    # checks to see if the sub function returns the expected output
    # based off of the given start and end indices and input list
    # should only include 3 and 4 since even though 5 is included in terms of index, it shouldn't be inclusive
    assert sub(input, start_index, end_index) == [3, 4]


def test_mutate_sub() -> None:
    input: list[int] = [1, 2, 3, 4, 5]
    start_index: int = 2
    end_index: int = 4
    sub(input, start_index, end_index)
    # checks to see if the function mutates the input list, which it shouldn't
    assert input == [1, 2, 3, 4, 5]


def test_empty_sub() -> None:
    input: list[int] = []
    start_index: int = 2
    end_index: int = 4
    # checks to see that the function returns an empty list when given one
    # even with start and end indices
    assert sub(input, start_index, end_index) == []


def test_list_add_at_index() -> None:
    input: list[int] = [2, 5, 6, 9, 10]
    add_value: int = 6
    value_index: int = 3
    add_at_index(input, add_value, value_index)
    # checks to see if the function returns the expected output
    # should insert the number 6 at index 3
    assert input == [2, 5, 6, 6, 9, 10]


def test_mutate_add_at_index() -> None:
    input: list[int] = [2, 5, 6, 9, 10]
    add_value: int = 6
    value_index: int = 3
    add_at_index(input, add_value, value_index)
    # checks to see whether the function mutates the input list, which it should
    # can just check to see if the input list is different from the original list
    # previous test checks for correct output
    assert input != [2, 5, 6, 9, 10]


def test_invalid_index_add_at_index() -> None:
    input: list[int] = [2, 5, 6, 9, 10]
    add_value: int = 6
    value_index: int = 6
    with pytest.raises(IndexError):
        add_at_index(input, add_value, value_index)
        # checks to see whether there is an IndexError raised if the value_index is outside the range of possible indices
