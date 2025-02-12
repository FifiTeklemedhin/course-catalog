import datetime

def military_to_time(military_time):
    """
    Converts a military time (integer) to a datetime.time object
    """
    
    return datetime.time(hour=military_time//100 , minute=military_time % 100)


def time_to_military(time_string, meridian_string):
    """
    Usage: `time_to_military('0130','PM') => 1330
    """

    cleaned_time = int(time_string)

    # first off, 12:xx should actually be 0:xx
    if int(cleaned_time / 100) == 12:
        cleaned_time -= 1200

    # now add 1200 to PMs
    if meridian_string == "PM":
        # e.g. 1:30pm == 1330 hours
        cleaned_time += 1200

    return cleaned_time

def minutes_since_midnight(military_time):
    """
    Converts a military time to a number of minutes since midnight
    Usage: minutes_since_midnight(1330) = 810
    """
    return 60*(military_time//100) + (military_time % 100)

def mround(n,i):
    """
    Rounds integer n to the nearest multiple of the integer i
    Usage: mround(29,5) => 30
    """
    if (i - (n % i)) <= (n % i):
        return (n // i) * (i + 1)
    else:
        return (n // i) * i