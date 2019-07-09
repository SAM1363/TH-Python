import re

def first_number(string):
    return re.search(r'\d',  string)    


def numbers(count, string):
    return re.search(r'\d'* count, string)


print(first_number('hello samson 1363'))
print(numbers(3, '13637676'))
