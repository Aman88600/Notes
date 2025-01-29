class Human:
    def __init__(self, name, height, age):
        self.__name = name 
        self.__height = height # Putting a double underscore before the variable makes it private
        self.__age = age

    # Now, I define the getter and setter methods inside the class, because private variables can only be changed from inside the class
    def get_height(self):
        print(self.__height)
    def set_height(self):
        new_height = int(input("Enter new Height : "))
        self.__height = new_height
aman = Human("Aman", 164, 22)
aman.get_height()
aman.set_height()
aman.get_height()