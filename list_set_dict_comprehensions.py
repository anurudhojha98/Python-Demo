
#comprehenstions

numbers=[2,3,4,5,8,6,7]

square=[]

for number in numbers:
    square.append(number*number)

print(square)

#list comprehntion
squared=[num*num for num in numbers]
print(squared)

squaredlist=[num*num for num in numbers if num % 2 == 0]
print(squaredlist)

#set comprehntion
setItems={num*num for num in numbers}
print(setItems)


#dict comprehntion

data={num:num*num for num in numbers}
print(data)