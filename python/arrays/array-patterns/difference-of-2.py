# https://www.codewars.com/kata/5340298112fa30e786000688/train/python


def twos_difference(lst):
    # Sort list and put in a set
    sorted_lst = sorted(lst)
    seen = set(sorted_lst)
    result = []
    # Loop through and check set membership
    for num in sorted_lst:
        if (num + 2) in seen:
            result.append((num, num + 2))
    return result
