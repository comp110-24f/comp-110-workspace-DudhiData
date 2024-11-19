"""Linked List Module!"""

from __future__ import annotations

__author__ = "730756130"


class Node:
    """Node class."""

    value: int  # declaring value and next variables
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        """Initializes value and next variables."""
        self.value = val
        self.next = next


def to_str(head: Node | None) -> str:
    """String representation of linked list."""
    if head is None:
        return "None"  # base case
    else:
        return f"{head.value} -> {to_str(head.next)}"  # recursive case


def last(head: Node) -> int:
    """Return last value of linked list."""
    if head.next is None:
        return head.value  # base case
    else:
        return last(head.next)  # recursive case


def value_at(head: Node | None, index: int) -> int:
    """Returning node data at given index."""
    if head is None:
        raise IndexError("Index out of bounds!")
    if index == 0:
        return head.value  # base case
    else:
        rest: int = value_at(head.next, index - 1)
        return rest  # recursive case


def max(head: Node | None) -> int:
    """Finding max value in linked list."""
    if head is None:
        raise ValueError("Cannot call max with None.")  # edge case
    if head.next is None:
        return head.value  # base case
    else:
        if (
            head.next.value > head.value
        ):  # checks to see if the node value is the highest
            head.value = (
                head.next.value
            )  # changes the current value to the next node's value
        else:
            head.next.value = head.value
            # if next node value not the highest, change it to the current highest value
        return max(head.next)  # recursive case


def linkify(nodes: list[int]) -> Node | None:
    """Turning list of integers into linked list."""
    if len(nodes) == 0:
        return None  # base case
    else:
        head: Node = Node(
            nodes[0], linkify(nodes[1:])
        )  # creates a linked list with sliced list
        return head  # recursive case


def scale(head: Node | None, factor: int) -> Node | None:
    """Scaling node values by given factor."""
    if head is None:
        return None  # base case
    else:
        rest: int = head.value * factor
        new_node: Node = Node(
            rest, scale(head.next, factor)
        )  # takes scaled value and creates new node
        return new_node  # recursive case


print(to_str(linkify([1, 2, 3])))
print(to_str(scale(linkify([1, 2, 3]), 2)))
courses: Node = Node(11990, Node(150, Node(1390, None)))
