import sys

def show():
    with open('data.txt') as file:
        for each in file:
            print(each)


def remenber(thing):
    with open('data.txt', 'a') as file:#open the file
        file.write(thing+'\n') # write thing in the file
    # file.close() 
    


if __name__ == '__main__':
    if sys.argv[1].lower() == '--list':
        show()
    else:
        remenber(' '.join(sys.argv[1:]))
    
