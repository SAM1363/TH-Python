dimensions = [
    (5, 5),
    (10, 10),
    (2.2, 2.3),
    (100, 100),
    (8, 70),
]

def area(data):
    return data[0] * data[1]

areas =  list(map(area, dimensions))
print(areas)