import datetime

birthdays = [
    datetime.datetime(2012, 4, 29),
    datetime.datetime(2006, 8, 9),
    datetime.datetime(1978, 5, 16),
    datetime.datetime(1981, 8, 15),
    datetime.datetime(2001, 7, 4),
    datetime.datetime(1999, 12, 30)
]

today = datetime.datetime.today()

def is_over_13(dt):
    delta = today - dt
    return delta.days >= 4745

# print(is_over_13(birthdays[0]))

def date_string(dt):
    return dt.strftime('%B %d')

# print(date_string(birthdays[0]))
birth_dates = map(date_string, filter(is_over_13, birthdays))

print(birth_dates)