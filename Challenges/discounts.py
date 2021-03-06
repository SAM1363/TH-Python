from functools import partial

prices = [
    10.50,
    9.99,
    0.25,
    1.50,
    8.79,
    101.25,
    8.00
]


def discount(price, amount):
    return price - price * (amount/100)

discount_10 = partial(discount, amount=10)

discount_25 = partial(discount, amount=25)

discount_50 = partial(discount, amount=50)

prices_10 = map(discount_10, prices)
print(list(prices_10))
prices_25 = map(discount_25, prices)
print(list(prices_25))
prices_50 = map(discount_50, prices)
print(list(prices_50))
