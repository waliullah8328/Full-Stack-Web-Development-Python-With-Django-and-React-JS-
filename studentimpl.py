from student import Student
class StudentImpl(Student):
    def __init__(self,student_first_name,student_last_name,dept):
        self.__student_first_name = student_first_name
        self.__student_last_name  = student_last_name
        self.__dept = dept
    
    def get_first_name(self):
        return self.__student_first_name

    def set_first_name(self, first_name):
        self.__student_first_name = first_name

    def get_last_name(self):
        return self.__student_last_name

    def set_last_name(self, last_name):
        self.__student_last_name =last_name

    def get_dept(self):
        return self.__dept

    def set_dept(self, dept):
        self.__dept = dept
    
   