# https://www.codewars.com/kata/52b305bec65ea40fe90007a7/train/python


def grabscrab(said, possible_words):
    said_hash = {}
    for s in said:
        said_hash[s] = said_hash.get(s, 0) + 1

    res = []

    for word in possible_words:
        hash = {}
        for letter in word:
            hash[letter] = hash.get(letter, 0) + 1
        if hash == said_hash:
            res.append(word)
        else:
            hash = {}
    return res


#     target_sorted = sorted(said)
#     return [word for word in possible_words if sorted(word) == target_sorted]
