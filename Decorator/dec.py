def outer():
    number = 5

    def inner():
        print('from inner', number)

    inner()

def apply(func, x, y):
    return func(x, y)


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


print('from outer {}'.format(outer()))

# print(apply(add, 3,6))
# print(apply(sub, 2, 9))

def close():

    x = 136
    def inner():
        print(x)

    return inner

result = close()
result()

def add_to_five(e):
    def inner():
        print(e+5)
    return inner

y = add_to_five(1358)
y()
