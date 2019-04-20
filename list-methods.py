list=[1,2,3,4,5,"anu"]

print(list.index(5))
print(list.index("anu"))

list2=["anurudh","ram",4,4.6,True]
list.extend(list2)
print(list)
index=list.index(True)
print(index)
list.append(4)
print(list)


list.insert(0,9)
print(list)

list.remove(5)
print(list)


list.remove(4)
print(list)


list.pop(4)
print(list)

list.pop()
print(list)


print(list.count(4))
list.reverse()
list.remove(True)
list.remove("anurudh")
list.remove("ram")
print(list)
list.sort()
print(list)

list3=list.copy()
list3.extend(list)
print(list3)

list.clear()
list2.clear()
list3.clear()
print(list)
print(list2)
print(list3)
