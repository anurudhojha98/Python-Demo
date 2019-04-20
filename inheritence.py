
from datetime import datetime as dt
class Person:
    continent='Europe'
    def __init__(self,first_name,last_name,email):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email

    def __str__(self):
        return "{} {} {}".format(self.first_name,self.last_name,self.email)

    def get_full_name(self):
        return "{} {}".format(self.first_name,self.last_name)

    @classmethod
    def get_continents(cls):
        return cls.continent[:2].upper()

    @staticmethod
    def get_current_time():
        return dt.now()


class Student(Person):
    pass

class Employee(Person):
    pass



if __name__=='__main__':
    personObj=Person('Anurudh','Ojha','a@gm.com')
    print(personObj.get_full_name())
    print(personObj.get_current_time())
    print(Person.get_continents())
    print(Person.get_current_time())

    studenObj=Student('Anu','Oj','a@oj.co')
    print(studenObj.get_full_name())
    print(studenObj.get_current_time())

    emplObj=Employee('AJ','Oj','aj@oj.co')
    print(emplObj.get_full_name())
    print(emplObj.get_current_time())


