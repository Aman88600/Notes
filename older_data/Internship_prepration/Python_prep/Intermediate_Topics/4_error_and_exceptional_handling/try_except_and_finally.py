number = input("Enter number : ")
try:
    number = int(number)
except ValueError: # Except block is required if try block is there, the exception can be specified or not
    print("Value Error")
except: # More than one except block can exist, depending on the situation
    print("Someting went wrong")
finally: # This always gets executed wheather exception is there or not
    print("This is Finally Block!")