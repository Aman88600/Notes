# In inheritance the child/sub class inherits properties from super/parent class
class Human: # Parent class
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        print(self.name)

class Student(Human): # Child Class
    def __init__(self, name, year):
        self.name = name
        self.year = year
        super().__init__(self.name) # Sending Info to parent class constructor


    def get_info(self):
        print(self.name, self.year)

obj = Student("Aman", 4)
obj.get_name()
obj.get_info()