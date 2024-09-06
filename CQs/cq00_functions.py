"""Functions CQ #0"""

__author__ = "730756130"


def mimic(message: str) -> str:
    """Returns message back to user"""
    return message


def main() -> None:
    """Print the result of calling mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
