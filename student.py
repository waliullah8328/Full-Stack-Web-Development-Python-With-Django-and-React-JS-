from abc import ABC,abstractclassmethod
class Student(ABC):
    @abstractclassmethod
    def get_first_name(self):
        pass
    @abstractclassmethod
    def set_first_name(self,first_name):
        pass
    @abstractclassmethod

    def get_last_name(self):
        pass
    @abstractclassmethod
    def set_last_name(self,last_name):
        pass
    @abstractclassmethod

    def get_dept(self):
        pass
    @abstractclassmethod
    def set_dept(self,dept):
        pass