
from datetime import datetime as dt
class NowMixin:
    @staticmethod
    def get_current_time():
        return dt.now()

class Person:

    def __init__(self,first_name,last_name,email):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email

    def __str__(self):
        return "{} {}".format(self.first_name,self.last_name)


    def get_full_name(self):
        return "{} {}".format(self.first_name,self.last_name)



class Student(NowMixin,Person):
    def __init__(self,first_name,last_name,email,school):
        super().__init__(first_name,last_name,email)
        self.school=school

    def get_full_name(self):
        return "{} {} {} {}".format(self.first_name, self.last_name,self.email,self.school)

class Employe(NowMixin,Person):
    def __init__(self,first_name,last_name,email,company):
        super().__init__(first_name,last_name,email)
        self.company=company

    def get_full_name(self):
        return "{} {} {} {}".format(self.first_name, self.last_name, self.email, self.company)


if __name__=='__main__':
    jon=Student("Anu","Ojha","a@123,com","RKGIT")
    ann=Employe("Raj","Sharma","raj@12.com","SBM Tech")

    print(jon.get_full_name())
    print(ann.get_full_name())


    print(jon.get_current_time())
    print(ann.get_current_time())





