from peewee import * 

db = SqliteDatabase('student.db')


class Student(Model):
    username = CharField(max_length=200, unique=True)
    points = IntegerField(default=0)

    class Meta:
        database = db

student = [
    {'username':'sam',
    'points': 8374169},
    {'username':'risako',
    'points': 3782348},
    {'username':'che',
    'points': 1208345},
    {'username':'adam',
    'points': 4762471},
]

def add_student():
    for each in student:
        try:
            Student.create(username=each['username'],
                            points=each['points'])
        except IntegrityError:
            student_record = Student.get(username=each['username'])
            student_record.points = each['points']
            student_record.save()
    
def top_student():
    student = Student.select().order_by(Student.points.desc()).get()
    return student


if __name__ == '__main__':
    db.connect()
    db.create_tables([Student], safe=True)
    add_student()
    print('our top student right now is {0.username} .'.format(top_student()))