"""Exercise 02 - a step towards making Wordle!"""

__author__ = "730625616"


def input_word() -> str:
    word = input("Enter a 5-character word: ")
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return word


def input_letter() -> str:
    character = input("Enter a single character: ")
    if len(character) != 1:
        print("Error: Character must be a single character.")
        exit()
    return character


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)
    count = 0
    # use if statements not elifs because we want all indexes to be considered
    if word[0] == letter:
        print(letter + " found at index 0")
        count = count + 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count = count + 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count = count + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count = count + 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count = count + 1
    # need to differentiate between when to say "None" versus the count
    if count == 0:  # only scenario to say "None" is if the count is 0
        print("No instances of " + letter + " found in " + word)
    if count == 1:  # need a specific case for 1 to print "instance" not "instances"
        print("1 instance of " + letter + " found in " + word)
    else:  # everything else is covered here, so that's why an else statement works
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
