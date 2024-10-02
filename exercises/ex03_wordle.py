"""Exercise 03 - Wordle"""

__author__ = "730625616"


def input_guess(secret_word_len: int) -> str:
    """Takes the user's guess and determines whether or not it's the right length"""
    word = input(f"Enter a {secret_word_len} character word: ")
    while len(word) != secret_word_len:
        word = input(f"That wasn't {secret_word_len} chars! Try again: ")
    # we will only reach this return statement if the while loop is exited
    return word


def contains_char(search_word: str, search_char: str) -> bool:
    """Checks whether or not a character is in a given word"""
    assert len(search_char) == 1
    index = 0
    while index < len(search_word):
        if search_char == search_word[index]:
            result = True
            # return stmt will exit the function -> won't reach the second return stmt
            return result
        else:
            index += 1
    # these two lines are only reached if we exit the while loop
    # only happens when character does not match anything in the word
    result = False
    return result


def emojified(guess: str, secret: str) -> str:
    """Displays the emoji representation of the guess"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index = 0
    # need to display all the boxes at once so add them to an initially empty string
    display = ""
    while index < len(secret):
        if guess[index] == secret[index]:
            display += GREEN_BOX
        elif contains_char(search_word=secret, search_char=guess[index]):
            display += YELLOW_BOX
        else:
            display += WHITE_BOX
        index += 1
    return display


def main(secret: str) -> None:
    """Entrypoint of the program and main game loop - organizes the game"""
    turn = 1
    unsolved = True
    turn_limit = 6
    while turn <= turn_limit and unsolved:
        print(f"===Turn {turn}/{turn_limit}===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        # need a condition for if it's solved so loop is exited
        if guess == secret:
            unsolved = False
        else:
            # need to update turn to eventually exit the loop
            turn += 1
    # different print stmts for if they won or lost
    if turn <= turn_limit:
        print(f"You won in {turn}/{turn_limit} turns!")
    else:
        print(f"X/{turn_limit} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
