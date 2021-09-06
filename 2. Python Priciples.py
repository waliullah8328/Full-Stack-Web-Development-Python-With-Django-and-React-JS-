# Object Oriented Programing Principle
# 1. Abstraction ---> planing
# 2. Encapsulation--> Security
# 3. Inheritance----> Code Reuse
# 4. Polymorphism---> User
# Class ---> Attribute,variable,function
class Student:
    stu_name = ""
    stu_dep  = ""
    def get_stu_info(self):
        return "Name : "+self.stu_name+"\nDepartment: "+self.stu_dep
student = Student()
student.stu_name ="Jahid Hasan"
student.stu_dep = "CSE"

student.stu_name ="Wali Ullah Ripon"
student.stu_dep = "CSE"

student.stu_name ="Jahid Hasan"
student.stu_dep = "CSE"
print(student.get_stu_info())

