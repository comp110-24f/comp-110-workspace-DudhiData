"""Concatenation File"""

__author__ = "730756130"


def concat(word_1: str, word_2: str) -> str:
    concat_string: str = str(word_1) + str(word_2)
    """Adds the first word to the second word"""
    return concat_string


if __name__ == "__main__":
    """Suppresses function call in this module for when we import concat function into visualize"""
    word1: str = "happy"
    word2: str = "tuesday"
    print(concat(word1, word2))
