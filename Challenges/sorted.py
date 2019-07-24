from operator import itemgetter

fruit_list = [
    ('banana', 5),
    ('coconut', 1),
    ('durian', 3),
    ('elderberries', 4),
    ('apple', 2)

]

sorted_fruit = sorted(fruit_list, key=itemgetter(0))

print(sorted_fruit)