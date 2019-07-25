pets = {'name':'Ernie', 'animal':'dog', 'breed':'Pug', 'age':2}

# for each in pets.items():
    # print(each)

def packing(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

# packing(name= 'samson', age='19', height= '177cm')


some_kinf_of_sequence = []

index = 1
for each in some_kinf_of_sequence:
    print(f'{index}, {each}')  # short cut for format starts with f'{}'
    # or
    print('{index}, {each}'.format(index, each))
    index =+ 1


for index, each in enumerate(some_kinf_of_sequence, 1): # same result but sort way hand using 'enumerate'
    print(index, each) # no need to use the format 


student_gpas = [4.0, 2.3, 3.5, 3.7, 3.9, 2.8, 1.5, 4.0]
