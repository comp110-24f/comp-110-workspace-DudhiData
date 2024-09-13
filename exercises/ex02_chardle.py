"""EX02 - Chardle"""

__author__ = "730756130"


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())
    """Control panel of all the code, calls input_word and input_letter as parameters, then uses those values as keyword arguments for contains_char"""


def input_word() -> str:
    user_word: str = input("Enter a 5-character word: ")
    if len(user_word) != 5:
        """user_word incompatible with code & stops program"""
        print("Error: Word must contain 5 characters.")
        exit()
    if len(user_word) == 5:
        """user_word compatible with program and returns the value to the main() function as a keyword argument for contains_char"""
        return user_word


def input_letter() -> str:
    user_letter: str = input("Enter a single character: ")
    if len(user_letter) != 1:
        print("Error: Character must be a single character.")
        """user_letter incompatible with code & stops program"""
        exit()
    if len(user_letter) == 1:
        """user_letter compatible with program and returns the value to the main() function as a keyword argument for contains_char"""
        return user_letter


def contains_char(word: str, letter: str) -> None:
    """# of instances a letter appears in a word, start at 0 and add 1 each time the boolean value is True"""
    matching_letter_count: int = 0
    print("Searching for " + letter + " in " + word)
    if word[0] == letter:
        print(letter + " found at index 0")
        matching_letter_count = matching_letter_count + 1
    if word[1] == letter:
        print(letter + " found at index 1")
        matching_letter_count = matching_letter_count + 1
    if word[2] == letter:
        print(letter + " found at index 2")
        matching_letter_count = matching_letter_count + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        matching_letter_count = matching_letter_count + 1
    if word[4] == letter:
        print(letter + " found at index 4")
        matching_letter_count = matching_letter_count + 1
    """Checks to see what the # of instances the letter appears is, 0 means no instances, 1 means a singular instance, while anything else has to be multiple instances"""
    if matching_letter_count == 0:
        print("No instances of " + letter + " found in " + word)
    elif matching_letter_count == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(
            str(matching_letter_count) + " instances of " + letter + " found in " + word
        )


if __name__ == "__main__":
    main()
"""Calls main() and begins the program"""
