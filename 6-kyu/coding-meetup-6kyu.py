# CODING MEETUP 7
def find_senior(lst):
    # === KING OF THE HILL ===
    # res = []
    # current_max_age = 0

    # for dev in lst:
    #     age = dev['age']

    #     # if age is higher than current, wipe list and set new current
    #     if age > current_max_age:
    #         current_max_age = age
    #         res = [dev]

    #     # if age is the same, append
    #     elif age == current_max_age:
    #         res.append(dev)

    # return res

    # === TWO PASS, record max, then match those == max ===

    max_age = max(dev["age"] for dev in lst)

    return [dev for dev in lst if dev["age"] == max_age]


# CODING MEETUP 8
def all_continents(lst):

    REQUIRED = {"Africa", "Americas", "Asia", "Europe", "Oceania"}

    found = {dev["continent"] for dev in lst}

    return found >= REQUIRED
