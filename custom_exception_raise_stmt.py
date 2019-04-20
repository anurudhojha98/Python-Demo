


students=[
    {"name":"anurudh","age":21,"email":"a@123.com"},
    {"name":"ajeet","email":"aj@123.com"},
    {"name":"ashish","age":29,"email":"ash@123.com"},
    {"name":"raj","email":"rj@123.com"}
]
class InvalidStudentException(Exception):
    pass

def display_student_info(data):
    for student in students:
        try:
            print("----------------")
            print(student['name'])
            print(student['age'])
            print(student['email'])
            print("----------------")
        except KeyError as e:
            print(e.__class__)
            raise InvalidStudentException("Invalid student record")








if __name__=='__main__':
    display_student_info(students)