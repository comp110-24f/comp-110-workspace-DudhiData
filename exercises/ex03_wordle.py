"""Wordle Exercise"""

__author__ = "730756130"


"""Start of program and main game loop"""


def main(secret: str) -> None:
    turn: int = 1
    """Declare the variable that will count the # of turns"""
    victory: bool = False
    """Declare the variable that will check whether the user has won or not"""
    while turn <= 6:
        """Repeats all of the other function code until the 7th turn"""
        print(f"=== Turn {turn}/6 ===")
        user_word: str = input_guess(5)
        """Declaring the variable that will store the user's input that we will use to check against secret to decide if victory is true or not"""
        print(emojified(user_word, secret))
        if user_word == secret:
            """Victory conditional, only activates when the user guesses correctly"""
            victory = True
        if victory:
            """If the previous conditional activates, then this means that the user has won and this conditional will check for a win or loss"""
            print(f"You won in {turn}/6 turns!")
            break
        turn += 1
    if not (victory):
        print("X/6 - Sorry, try again tomorrow!")
        """If victory remains false even after 6 turns, then the user loses"""


def input_guess(secret_char_value: int) -> str:
    input_user_word = input(f"Enter a {secret_char_value} character word: ")
    """Declares the variable that will hold the user input for this function's purposes"""
    while secret_char_value != len(input_user_word):
        """Repeats the user input question until the length of the user input matches the selected value of 5"""
        input_user_word = input(f"That wasn't {secret_char_value} chars! Try again: ")
    return input_user_word


"""Checks to see whether the second parameter is present in the first parameter"""


def contains_char(secret_word: str, char_guess: str) -> bool:
    assert len(char_guess) == 1
    """Makes sure the second parameter is only 1 character long"""
    index: int = 0
    while index <= len(secret_word) - 1:
        """Iterates through the secret word"""
        if secret_word[index] == char_guess:
            """If a certain letter of the secret word matches the character guess, then show that at least one character in the user's guess is present"""
            return True
        index += 1
    if (index - 1 == len(secret_word) - 1) and (secret_word[index - 1] != char_guess):
        """Lower index to an acceptable range, allowing us to check if all character of secret have been iterated through, and if that last letter doesn't equal the character guess, return False"""
        return False
    exit()


"""Returns a string of emojis that will tell whether a character in the guess is in the correct position, present but in the wrong position, or not present at all"""


def emojified(user_word: str, hidden_word: str) -> str:
    assert len(user_word) == len(hidden_word)
    """Makes sure the lengths of both parameters match"""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    emoji_string: str = ""
    """Declaring placeholder variable we will append to, then return for printing"""
    while index <= len(user_word) - 1:
        """Iterates 5 times, but could change depending on secret_char_value"""
        if user_word[index] == hidden_word[index]:
            """Checks to see if the character of the word guessed matches the character of the secret word"""
            emoji_string += GREEN_BOX
        elif contains_char(hidden_word, user_word[index]):
            """Since the position doesn't match, we check to see if it is at least present through contain_char"""
            emoji_string += YELLOW_BOX
        else:
            """If it doesn't match and it isn't present, that means the letter is not there at all"""
            emoji_string += WHITE_BOX
        index += 1
    return emoji_string


if __name__ == "__main__":
    """Gives us our secret word to work with, can be changed or set to a database of words"""
    main(secret="codes")
