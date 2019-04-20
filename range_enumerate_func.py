

#Range method is used for iterations


for i in range(10):
    print(i)

print("this is with range")

for i in range(2,10):
    print(i)

print("this is with range")

for i in range(2,10,2):
    print(i)

#enumerate function is used for usually print the index

listItem=["NA","PA","SA","TA"]

index=0
for i in listItem:
    index+=1
    print("{}.{}".format(index,i))

#by enumerate function

for index,i in enumerate(listItem):
    print("{}.{}".format(index+1,i))