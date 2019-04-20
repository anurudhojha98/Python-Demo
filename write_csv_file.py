#
import csv

with open('students.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    studentsInfo=[
        {'first_name': 'ANurudh', 'last_name': 'Beans'},
        {'first_name': 'Lovely', 'last_name': 'Spam'},
        {'first_name': 'Wonderful', 'last_name': 'Spam'}
                  ]
    writer.writeheader()

    for student in studentsInfo:
        writer.writerow(student)


#
# with open("students.csv","w") as f:
#     """First way"""
    # writer=csv.writer(f)
    #
    # headings=["Name","Email","Age"]
    #
    # writer.writerow(headings)
    #
    # data=[
    #     ['Anurudh','anurudh@gm.co',23],
    #     ['aj', 'aj@gm.co', 29],
    #     ['ash', 'ash@gm.co', 25]
    # # ]
    # """Second Way"""


