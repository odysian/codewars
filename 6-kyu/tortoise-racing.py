def race(v1, v2, g):
    if v1 > v2:
        return None

    # ALWAYS CONVERT TO SMALLEST UNIT
    time_hours = g / (v2 - v1)
    time_seconds = int(time_hours * 3600)

    hours = time_seconds // 3600
    minutes = (time_seconds % 3600) // 60
    seconds = time_seconds % 60

    return [hours, minutes, seconds]
