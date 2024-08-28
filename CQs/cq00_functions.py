"""My first challenge question in COMP 110 :)"""

__author__ = "730625616"


def mimic(message: str) -> str:
    """Returns your message back to you"""
    return message


def main() -> None:
    """prints the results of mimic"""
    print(mimic(message=input("What is your message? ")))


if __name__ == "__main__":
    main()
