

students=[
    {"name":"anurudh","age":21,"email":"a@123.com"},
    {"name":"ajeet","email":"aj@123.com"},
    {"name":"ashish","age":29,"email":"ash@123.com"},
    {"name":"raj","email":"rj@123.com"}
]

def display_student_info(data):
    for student in students:
        try:
            print("----------------")
            print(student['name'])
            print(student['age'])
            print(student['email'])
            print("----------------")
        except KeyError:
            continue







if __name__=='__main__':
    display_student_info(students)