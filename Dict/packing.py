def pack(**x):
    print(x)


def unpack(Fname=None, Lname=None):
    if Fname and Lname:
        print('Hi {} {}'.format(Fname, Lname))
    else:
        print('hey no name')


pack(name="sam", num=136, sleep=None)

unpack(**{'Fname':'samson', 'Lname':'blankenship'})
