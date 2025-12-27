def count_developers(lst):
    # Sum 1 for every developer where continent is Europe AND language is JS
    return sum(
        1
        for dev in lst
        if dev["continent"] == "Europe" and dev["language"] == "JavaScript"
    )
