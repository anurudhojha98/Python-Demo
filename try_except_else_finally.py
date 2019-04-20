
class Persson:
    students = [
        {"name": "anurudh", "age": 21, "email": "a@123.com"},
        {"name": "ajeet", "email": "aj@123.com"},
        {"name": "ashish", "age": 29, "email": "ash@123.com"},
        {"name": "raj", "email": "rj@123.com"}
    ]

    def __init__(self):
        pass
    @classmethod
    def display_stu_info(cls):
        for stu in cls.students:
            try:
                name=stu['name']
                age=stu['age']
                email=stu['email']
            except KeyError:
                continue
            else:
                print("--------------")
                print(name)
                print(age)
                print(email)
                print("--------------")
            finally:
                print("Finally executed")

if __name__=="__main__":
    person=Persson()
    print(person.display_stu_info())





