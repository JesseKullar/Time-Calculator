def round_down(num, divisor):
    return num - (num % divisor)


def add_time(start, duration, weekday=""):
    ampm = {'AM': 1, 'PM': -1}
    week = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2,
            'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
    [time, ampm_start] = start.split()
    [hour_start, min_start] = time.split(':')
    [hour_duration, min_duration] = duration.split(':')
    total_min = int(min_start) + int(min_duration)

    add_hour = int()
    while total_min >= 60:
        total_min -= 60
        add_hour += 1

    days_passed = int()
    ampm_passed = 1
    total_hour = int(hour_start) + int(hour_duration) + add_hour
    if total_hour == 12:
        ampm_passed *= -1
    while total_hour > 12:
        total_hour -= 12
        ampm_passed *= -1
        days_passed += 0.5
        if total_hour == 12:
            ampm_passed *= -1
            days_passed += 0.5
    for val in ampm.values():
        if val == ampm[ampm_start] * ampm_passed:
            new_ampm = list(ampm.keys())[list(ampm.values()).index(val)]

    new_time = str(total_hour) + ':' + str(total_min).rjust(2, '0') + ' ' + new_ampm

    if ampm_start == 'AM':
        days_passed = round_down(days_passed, 1)

        if weekday:
            weekday_val = week[weekday.title()] + int(days_passed)
            while weekday_val > 7:
                weekday_val -= 7
            new_weekday = list(week.keys())[list(week.values()).index(weekday_val)]
            new_time += ', ' + new_weekday

        if days_passed > 0:
            if days_passed == 1:
                new_time += ' (next day)'
            else:
                new_time += ' (' + str(int(days_passed)) + ' days later)'

    elif ampm_start == 'PM':

        if weekday:
            weekday_val = week[weekday.title()] + int(days_passed + 0.5)
            while weekday_val >= 7:
                weekday_val -= 7
            new_weekday = list(week.keys())[list(week.values()).index(weekday_val)]
            new_time += ', ' + new_weekday

        if days_passed > 0:
            if days_passed == 0.5:
                new_time += ' (next day)'
            else:
                new_time += ' (' + str(int(days_passed + 0.5)) + ' days later)'

    return new_time
