# Exception Handeling
"""file = open("file2.txt","r")
for i in file.readline():
    print(i,end = "")
    """

try:
    file = open("file2.txt", "r")
    for i in file.readline():
        print(i, end="")
except Exception as e:
    print(e)


print()
print(100/10)
print(100/5)
print(100/20)
# function Exception Handeling
text = "Loren"
def file_handeling(file_name, mode, text=""):
    try:
        if mode == "r":
            file = open(file_name, mode)
            for i in file.readline():
                print(i, end="")
                file.close()
        else:
            file = open(file_name, mode)
            file.write(text)
            file.close()

    except Exception as e:
        print(e)
file_name = "file1.text"
mode = "r"
file_handeling(file_name, mode, text)