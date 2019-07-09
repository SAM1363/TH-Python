import datetime

naive = datetime.datetime(2019, 7, 2, 11, 13)

pacific = datetime.timezone(datetime.timedelta(hours=-8))
europe = datetime.timezone(datetime.timedelta(hours=+1))

hill_valley = datetime.datetime(2019, 7, 2, 11, 13, tzinfo=pacific)
paris = hill_valley.astimezone(europe)

print(paris)