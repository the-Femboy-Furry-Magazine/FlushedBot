import time
import math

start_time = time.time()

to_minutes = lambda epoch: math.floor(epoch / 60)
to_hours = lambda epoch: math.floor(epoch / 3600)
to_days = lambda epoch: math.floor(epoch / 216000)


def uptime(start=start_time):
    current_time = time.time()
    difference = math.floor(current_time - start)
    seconds = difference % 60

    seconds_unit = "second" if seconds == 1 else "seconds"
    output = f"{seconds} {seconds_unit}"

    minutes = to_minutes(difference)
    if not minutes:
        return output

    minutes = minutes % 60
    minute_unit = "minute" if minutes == 1 else "minutes"
    output = f"{minutes} {minute_unit}, and " + output

    hours = to_hours(difference)
    if not hours:
        return output

    hours = hours % 24
    hours_unit = "hour" if hours == 1 else "hours"
    output = f"{hours} {hours_unit}, " + output

    days = to_days(difference)
    if not days:
        return output

    days_unit = "day" if days == 1 else "days"
    output = f"{days} {days_unit}, " + output

    return output


time.sleep(1)

print(uptime())