# for instance ...
# combo([1, 2, 3], 'abc')
# Output:
# [(1, 'a'), (2, 'b'), (3, 'c')]

CM = {
    'PythonBasic': 320,
    'HTMLBasic': 270,
    'Sass': 300,
    'WordPress': 400
}


for C, M in CM.items():
    print('{}: {}minuits'.format(C, M))


for index, M in enumerate(CM, start=1):
    print('{}: {}minuits'.format(index, M))


def combo(*arg):
    result = []
    for index, value in enumerate(arg[0]):
        result.append((value, arg[1][index]))
    return result


def combo(*arg):
    result = []
    for index, value in enumerate(arg[0]):
        result.append((value, arg[1][index]))
    return result 

print(combo([1, 2, 3, 4], 'abcs'))


count = 1
for each in 'samsonblankenship':
    print('{}: {}'.format(count, each))
    count += 1

