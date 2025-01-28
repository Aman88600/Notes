# small anonymous functions that can take any number of arguments but can only have one expression
x = lambda :42
print(x())

x = lambda i : i * 2
print(x(10))