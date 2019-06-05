books = [
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]

elements = [
    "Hydrogen",
    "Helium",
    "Lithium",
    "Symposium",
    "Beryllium",
    "Boron",
    "Carbon",
]

incorrect = elements.pop(3)
print("{} is not an element".format(incorrect))

classics = [
    "The Mona Lisa",
    "Starry Night",
    "The Scream",
    "Guernica",
    "The Persistence of Memory",
]

painting = classics.pop()
print(painting)


surname = "Rasputin"
advisor = surname
del surname
print(advisor)


options = [
    "rock",
    "paper",
    "scissors",
    "flamethrower",
]

del options[3]
print('there are {} options'.format(len(options)))