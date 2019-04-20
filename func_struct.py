

#function writing


def hello():
    greetings="Hello Friends! I have met before you"
    print(greetings)

greet=hello()

print(greet)


def display_values():
    display_values="Hello Friends! I will not be meet you ever"
    return  display_values;

greetings=display_values()
print(greetings)


def numers_sum(num1,num2,num3):
    sum=num1+num2+num3
    return sum

print(numers_sum(2,4,5))


def funct_test(num1,num2,num3=8):
    sum=num1+num2+num3
    return sum

print(funct_test(3,5,4))


def pos_args_test(num1,*args,**kargs):
    for arg in args:
        tsum=num1+sum(arg)
        print(tsum)
    for k,v in kargs.items():
        print(k,v)

value=[4,5,6,7]
dvalue={"name":'ANU',"age":43}
total=pos_args_test(3,value,**dvalue)

print(total)