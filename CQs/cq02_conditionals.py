"""Conditinals Challenge Question"""

__author__ = "730756130"


def guess_a_number() -> None:
    secret: int = 7
    # number user is guessing
    x: int = int(input("Guess a number: "))
    # user guess number
    print("Your guess was " + str(x) + ".")
    if x == secret:
        print("You got it!")
        # user guess equals secret number
    if x < secret:
        print("Your guess was too low! The secret number is " + str(secret) + ".")
        # user guess is lower than secret number
    if x > secret:
        print("Your guess was too high! The secret number is " + str(secret) + ".")
        # user guess is higher than secret number


if __name__ == "__main__":
    guess_a_number()
    # calling function
