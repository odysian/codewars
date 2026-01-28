# https://www.codewars.com/kata/55eeddff3f64c954c2000059/train/python

from itertools import groupby


def sum_consecutives(lst):
    last_seen = lst[0]
    curr_sum = lst[0]
    res = []
    for i in range(1, len(lst)):
        current = lst[i]
        if current == last_seen:
            curr_sum += current
        else:
            res.append(curr_sum)
            last_seen = current
            curr_sum = current
    res.append(curr_sum)
    return res

    # Group by one liner
    return [sum(group) for key, group in groupby(lst)]
