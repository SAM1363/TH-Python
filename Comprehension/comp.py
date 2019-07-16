comp1 = [num * 2 for num in range(1, 6)]

comp2 = {letter: num for letter, num in zip('abcdef', range(1, 7))}

comp3 = {num * 2 for num in [5, 2, 18, 2, 42, 2, 2]}

print(comp1)
print(comp2)
print(comp3)