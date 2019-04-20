

class Person:

    def __init__(self,first_name,last_name,email):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email

    def __str__(self):
        return "{} {} {}".format(self.first_name,self.last_name,self.email)

if __name__=='__main__':
    joe=Person('Anurudh','Ojha','anu@gm.com')
    print(str(joe))