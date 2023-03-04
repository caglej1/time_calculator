'''
https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator
'''

def add_time(start_time, duration, start_day=None):
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    # Parse needed values
    is_am = True if start_time.split()[1] == "AM" else False
    curr_hours = int(start_time.split(':')[0])
    curr_mins = int(start_time.split(':')[1].split()[0])
    hours_to_add, mins_to_add = map(int, duration.split(':'))

    # Find resulting minutes
    min_overflow = 0
    future_mins = curr_mins + mins_to_add
    if future_mins >= 60:
        future_mins %= 60
        min_overflow = 1

    # Find resulting hours, days later, and if AM or PM
    (days_later, hours_remaining) = divmod(hours_to_add, 24)
    future_hours = curr_hours + hours_remaining + min_overflow
    if future_hours >= 12:
        (hours_overflow, future_hours) = divmod(future_hours, 12)
        future_hours = future_hours if future_hours != 0 else 12
        if hours_overflow % 2 != 0 or future_hours == 12:
            if not is_am:
                days_later += 1
            is_am = not is_am

    am_or_pm = "AM" if is_am else "PM"

    # Construct and return resulting time
    return_time = "{}:{:0>2d} {}".format(future_hours, future_mins, am_or_pm)

    if start_day != None:
        future_day = days[(days.index(start_day.casefold()) + days_later) % 7].capitalize()
        return_time += f", {future_day}"

    if days_later == 1:
        return_time += " (next day)"
    elif days_later > 1:
        return_time += f" ({days_later} days later)"

    return return_time
