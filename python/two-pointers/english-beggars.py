# https://www.codewars.com/kata/59547688d8e005759e000092/train/python
# 7 kyu
def distribution_of(golds):
    a = 0
    b = 0
    l = 0
    r = len(golds) - 1
    turn = "a"

    while l <= r:
        if golds[l] >= golds[r]:
            current_gold = golds[l]
            l += 1
        else:
            current_gold = golds[r]
            r -= 1

        if turn == "a":
            a += current_gold
            turn = "b"
        else:
            b += current_gold
            turn = "a"
    return [a, b]


# https://www.codewars.com/kata/59590976838112bfea0000fa/train/python
# 6 kyu
def beggars(values, n):
    if n == 0:
        return []
    turn = 0
    res = [0] * n

    for i in range(len(values)):
        current_gold = values[i]
        res[turn] += current_gold
        turn = (turn + 1) % n

    return res
