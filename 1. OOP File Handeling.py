# OOP _- Object Oriented Programing
def create_file(file_name, mode, data):
    file = open(file_name, mode)
    file.write(data)
    file.close()

file_name = "file2.txt"
mode = "a"
data = "Hello"
create_file(file_name, mode, data)

for i in range(3,7):
    file_name = "file" + str(i)+".docx"
    mode = "w"
    data = "This file no"+str(i)
    create_file(file_name, mode, data)