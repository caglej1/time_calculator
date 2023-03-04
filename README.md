# Overview
Write a function named `add_time` that takes in two required parameters and one optional parameter:

  * a start time in the 12-hour clock format (ending in AM or PM)
  * a duration time that indicates the number of hours and minutes
  * (optional) a starting day of the week, case insensitive

The function should add the duration time to the start time and return the result.

## Rules
Do not import any Python libraries. Assume that the start times are valid times. The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number.

If the result will be the next day, it should show `(next day)` after the time. If the result will be more than one day later, it should show `(n days later)` after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.

## Example

```python
add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
```

## My Solution
First, I declared a function that accepts three parameters:
  * `start_time` is the initial time that will be updated by the function.
  * `duration` is the amount of time to add to `start_time`.
  * `start_day` is an optional parameter indicating the starting day of the week.
Additionally, I created a lookup list of every day of the week.
```python
def add_time(start_time, duration, start_day=None):
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
```

I parsed the current half of the day (AM/PM) along with the hours and minutes of `start_time` and `duration`.
```python
is_am = True if start_time.split()[1] == "AM" else False
curr_hours = int(start_time.split(':')[0])
curr_mins = int(start_time.split(':')[1].split()[0])
hours_to_add, mins_to_add = map(int, duration.split(':'))
```

I calculated the resulting minutes, accounting for possible overflow.
```python
min_overflow = 0
future_mins = curr_mins + mins_to_add
if future_mins >= 60:
    future_mins %= 60
    min_overflow = 1
```

I calculated the resulting hours, days later, and half of the day (AM/PM).
```python
(days_later, hours_remaining) = divmod(hours_to_add, 24)
future_hours = curr_hours + hours_remaining + min_overflow
if future_hours >= 12:
    (hours_overflow, future_hours) = divmod(future_hours, 12)
    future_hours = future_hours if future_hours != 0 else 12
    if hours_overflow % 2 != 0 or future_hours == 12:
        if not is_am:
            days_later += 1
        is_am = not is_am
```

Finally, I constructed, formatted, and returned the resulting time.
```python
am_or_pm = "AM" if is_am else "PM"
return_time = "{}:{:0>2d} {}".format(future_hours, future_mins, am_or_pm)

if start_day != None:
    future_day = days[(days.index(start_day.casefold()) + days_later) % 7].capitalize()
    return_time += f", {future_day}"

if days_later == 1:
    return_time += " (next day)"
elif days_later > 1:
    return_time += f" ({days_later} days later)"

return return_time
```

Proper execution can be verified by executing the unit tests [here](https://replit.com/@caglej1/boilerplate-time-calculator#time_calculator.py).
