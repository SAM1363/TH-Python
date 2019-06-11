def num_teachers(member):
    num = 0
    for each in member:
        num += 1
    return  num


def num_courses(course):
    num = 0
    for each in course.values():
        num += len(each)
    return num



    