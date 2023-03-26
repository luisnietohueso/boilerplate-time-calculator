def add_time(start_time, duration, starting_day=None):
    WEEKDAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    start_time, period = start_time.split()
    hours, minutes = start_time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    if period == "PM":
        hours += 12
    duration_hours, duration_minutes = duration.split(":")
    duration_hours = int(duration_hours)
    duration_minutes = int(duration_minutes)
    hours += duration_hours
    minutes += duration_minutes
    if minutes >= 60:
        minutes -= 60
        hours += 1
    days_later = hours // 24
    hours = hours % 24
    new_period = "AM"
    if hours >= 12:
        new_period = "PM"
    if hours > 12:
        hours -= 12
    elif hours == 0:
        hours = 12
    minutes = str(minutes).rjust(2, "0")
    new_time = f"{hours}:{minutes} {new_period}"
    if starting_day:
        starting_day = starting_day.lower()
        starting_index = WEEKDAYS.index(starting_day)
        ending_index = (starting_index + days_later) % 7
        new_day = WEEKDAYS[ending_index]
        new_time += f", {new_day.title()}"
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"
    return new_time
