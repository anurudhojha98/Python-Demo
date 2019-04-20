from datetime import datetime as dt

class Person:
    continent='Asia'

    def __init__(self,first_name,last_name,email):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email

    def __str__(self):
        return "{} {} ".format(self.first_name,self.last_name)

    @classmethod
    def get_continent_abbr(cls):
        abbr= cls.continent[:2].upper()
        return abbr

    @staticmethod
    def current_date():
        return dt.now()




if __name__=="__main__":
    person=Person('Anu','Ojha','anu@gm.com')
    print(str(person))
    print(Person.continent)
    print(Person.get_continent_abbr())
    print(Person.current_date())
    print(person.current_date())

