"""Defining dictionary utility functions"""

__author__ = "730625616"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Returns a new dictionary with inverted keys and values of the input dictionary"""
    new_dict = {}
    for key in input_dict:
        if input_dict[key] in new_dict:
            # error is raised if the new key being added already exists
            raise KeyError("Duplicate key attempted")
        new_dict[input_dict[key]] = key
    return new_dict


def favorite_color(colors: dict[str, str]) -> str:
    """Determines the most frequently occuring color in a list of favorite colors"""
    counts: dict[str, int] = {}
    for name in colors:
        colors[name].lower()
        if colors[name] in counts:
            # updates the value if the color is already a key in counts
            counts[colors[name]] += 1
        else:
            # creates a value for the key in counts if the key doesn't already exist
            counts[colors[name]] = 1
    # print(counts) <- used during the coding process to make sure counts are correct
    max_count: int = 0
    fav_color: str = ""
    for color in counts:
        # compares the counts values to find the maximum count and associated color
        if counts[color] > max_count:
            max_count = counts[color]
            fav_color = color
    return fav_color


def count(input_list: list[str]) -> dict[str, int]:
    """Returns a dictionary with counts of each word in a list"""
    # initializing the counts dictionary
    counts: dict[str, int] = {}
    for elem in input_list:
        if elem in counts:
            counts[elem] += 1
        else:
            counts[elem] = 1
    return counts


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Creates a dictionary with letters as keys and words from the input list starting with that letter as values"""
    alphabet: dict[str, list[str]] = {}
    for word in words:
        # ensures that upper and lowercase letters are treated as the same letter
        word = word.lower()
        letter = word[0]
        if letter in alphabet:
            # adds the word to the list if the letter is already a key
            alphabet[letter].append(word)
        else:
            # creates a new key-value pair if the letter is not already a key
            alphabet[letter] = [word]
    return alphabet


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Updates an existing dictionary to reflect student attendance"""
    # checks if the day is already in the dictionary
    if day in attendance:
        # if it is, checks if the student is already listed or not
        if student not in attendance[day]:
            attendance[day].append(student)
    # makes a new key for the day if not already in the dictionary
    else:
        attendance[day] = [student]
