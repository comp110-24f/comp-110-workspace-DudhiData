"""Coordinates File"""

__author__ = "730756130"


def get_coords(xs: str, ys: str) -> None:
    index_xs: int = 0
    index_ys: int = 0
    """Establishes indices for both words for when we repeat through them"""
    coords: str = ""
    """Declare a placeholder variable that we will append the coordinate letters to"""
    while index_xs <= len(xs) - 1:
        """Repeats while the index for xs is less than or equal to the length of xs - 1 (to account for Python indices starting at 0)"""
        while index_ys <= len(ys) - 1:
            """Same as the repeat condition for the parent loop instead for ys and index_ys"""
            coords = "(" + xs[index_xs] + ", "
            """Establishes first part of coordinate we will return"""
            coords = coords + ys[index_ys] + ")"
            """Appending each letter of ys to the initial coordinate through the use of the relative reassignment operator"""
            print(coords)
            index_ys += 1
        index_xs += 1
        """Starts next set of coordinates with the next letter of xs as the initial coordinate"""
        index_ys = 0
        """Resets index_ys so we can reiterate through the rest of ys and reappend them to the new initial coordinate"""


get_coords("zebra", "bye")
