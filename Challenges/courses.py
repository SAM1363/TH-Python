# The dictionary will look something like:
# {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}nu
#
# Each key will be a Teacher and the value will be a list of courses.
#
# Your code goes below here.


def num_teachers(num):  # count the number of the items
    return len(num)


def num_courses(num):  # count(len) and adding(sum) the each item inside the of values
    return sum(len(each) for each in num.values())


def courses(c):  # extract the each value and gather into a single list, adding list into another could be used extend()
    courses = []
    for each in c.values():
        courses.extend(each)
    return courses.append(each)


def courses2(c):  # doing the same thing with the above, just using append method for each value
    courses = []
    for each in c.values():
        for e in each:
            courses.append(e)
    return courses


def most_courses(c):
    l_num = 0
    l_teacher = ' '
    for each in c:
        class_num = len(c[each])
        if(class_num > l_num):
            class_num = l_num
            l_teacher = each
    return l_teacher


def stats(dic):
    main_list = []
    for teacher, course in dic.item():
        total = 0
        for value in dic.values():
            for course in value:
                total += 1
                main_list.append([teacher, total])
    return main_list


def stats(t_dict):  # same result with above , cant understand how it's working
    all_courses = []
    for teacher in t_dict:
        all_courses.append([teacher, len(t_dict[teacher])])
    return all_courses