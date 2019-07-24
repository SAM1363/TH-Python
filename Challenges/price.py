from operator import add
from functools import reduce

prices = [
    (6.99, 5),
    (2.94, 15),
    (156.99, 2),
    (99.99, 4),
    (1.82, 102)
]


def product_sales(each):
    x = each[0] * each[1]
    return x

total = [reduce(add, list(map(product_sales, prices)))]
print(total)


