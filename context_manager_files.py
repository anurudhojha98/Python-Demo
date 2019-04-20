

with open("Context_manager_file.txt","w") as file_obj:
    for txt in range(1,10):
        file_obj.write(" This is line number {}.\n".format(txt))
