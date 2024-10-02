"""Creating and using the concat function"""

__author__ = "730625616"


def concat(string_1: str, string_2: str) -> str:
    new_string = string_1 + string_2
    return new_string


word1 = "happy"
word2 = "tuesday"

if __name__ == "__main__":
    print(concat(word1, word2))
