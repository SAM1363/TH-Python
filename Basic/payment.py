import math


def split_check(total, number_of_people):
    if number_of_people > 1:
        return math.ceil(total / number_of_people)

try:
    the_amount = float(input('What is the total? '))
    people = int(input('What is the number of people? '))
    per_person = split_check(the_amount, people)
    print('It is ${} per person!'.format(per_person))
except NameError:
    print('that is not a valid value')
else:
    print('have to be more than a person')

  