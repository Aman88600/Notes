# To create a class we use the "class" keyword
class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    # This is a method/function of the class
    def get_student_info(self):
        return [self.name, self.year]

# Now we make an instance of the class, knows as object
obj = Student("Aman", 4)
print(obj.name) # we can access the class variables, called attributes using object
print(obj.get_student_info()) # we can also access the class methods using object