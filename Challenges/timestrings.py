## Examples
# to_string(datetime_object) => "24 September 2012"
# from_string("09/24/12 18:30", "%m/%d/%y %H:%M") => datetime
import datetime


def to_string(today):
    return today.strftime("%m/%d/%y %H:%M")


def from_string(arg1, arg2):
    return datetime.datetime.strptime(arg1, arg2)

now = datetime.datetime.now()
print(to_string(now))

print(from_string(to_string(now), "%m/%d/%y %H:%M"))