# https://www.codewars.com/kata/5878520d52628a092f0002d0/train/python


# Manual labor, down in the mines
def string_transformer(s):
    words = s.split(" ")
    res = []

    for word in words:
        new_word = []
        for letter in word:
            if letter.isupper():
                new_word.append(letter.lower())
            else:
                new_word.append(letter.upper())
        res.append("".join(new_word))
    return " ".join(res[::-1])


# Clean solution using swapcase()
def string_transformer1(s):
    swapped = s.swapcase()
    words = swapped.split(" ")
    return " ".join(words[::-1])
