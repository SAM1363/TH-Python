import re


def find_words(num, data):
    return re.findall('\w+' * num, data)


def find_words2(count, data):
    return re.findall('\w{{{:d},}}'.format(count), data)


print(find_words2(4, 'samson, blankenship, che, nakamura'))