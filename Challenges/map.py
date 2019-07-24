backwards = [
    'tac',
    'esuoheerT',
    'htenneK',
    [5, 4, 3, 2, 1],
]

def reverse(item):
    return item[::-1]


has_reversed = list(map(reverse, backwards))
print(has_reversed)
# for each in backwards:
#     print(each[::-1])