def simple_decorator(function):
    def wrapper():
        print("Before")
        function()
        print("After")
    return wrapper

@simple_decorator
def hello():
    print("Hello")

hello()

def twice(function): # function here
    def wrapper(*args, **kwargs): # arguments here
        function(*args, **kwargs)
        function(*args, **kwargs)
    return wrapper

@twice
def greet(name):
    print(f"Hello, {name}")

greet("Aman")