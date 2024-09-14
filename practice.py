def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="hi", letter="h"))

print(check_first_letter(word="hi", letter="j"))
