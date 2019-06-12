COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

# for each, value in COURSES.items():
#         print(each)
#         print(value)
#         print('-' * 20)


# def covers(dic):
#     course_name = []
#     for key, value in COURSES.items():
#         if value & dic:
#             course_name.append(key)
#     return course_name


def covers_all(dic):
    courses = []
    for key, value in COURSES.items():
        if dic.issubset(value):
            courses.append(key)
    return courses

print(covers_all({"conditions", "input"}))
    