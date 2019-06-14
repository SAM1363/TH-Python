def combiner(lists):
    num = 0
    string = ''
    for each in lists:
        if isinstance(each, str): 
                string += each
        elif isinstance(each, float):
                num += each
        elif isinstance(each, int):
                num += each

    return '{}{}'.format(string, num)


print(combiner(["apple", 5.2, "dog", 8]))
