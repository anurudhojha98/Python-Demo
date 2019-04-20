
#
# file_object=open("customers.txt","w")
#
# file_object.write("This is new line")
#
# file_object.close()

with open("Context_manager_file.txt","r") as file_Object:
   # print(file_Object.read())
    # print(file_Object.readline())
     print(file_Object.readlines())