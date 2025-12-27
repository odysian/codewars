# CODING MEETUP 1
def count_developers(lst):
    # Sum 1 for every developer where continent is Europe AND language is JS
    return sum(
        1
        for dev in lst
        if dev["continent"] == "Europe" and dev["language"] == "JavaScript"
    )


# CODING MEETUP 2
def greet_developers(lst):

    for dev in lst:
        dev["greeting"] = (
            f"Hi {dev['firstName']}, what do you like the most about {dev['language']}?"
        )

    return lst
