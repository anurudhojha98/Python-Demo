

#Nested loops


data=[
    {"name":"Anu",
     "age":21
     },
    {"name":"AJ",
     "age":26
     },
    {"name":"AS",
     "age":29
     }
]

#first option

for person in data:
    for name,age in person.items():
        print(" {}. {}".format(name,age))


names=["Anurudh","Ajay","Raj","Ashish"]
ages=[21,26,27,29]

for name,age in zip(names,ages):
    print("{},{}".format(name,age))