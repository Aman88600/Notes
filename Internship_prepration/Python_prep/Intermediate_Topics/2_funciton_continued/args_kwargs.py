#*args and **kwargs are used to allow functions to accept an arbitrary number of arguments. 
#These features provide flexibility when designing functions that need to handle a varying number of inputs.

# *args
def sum(*args):
    new_sum = 0
    for i in args:
        new_sum += i
    return new_sum
print(sum(1,2))
print(sum(1,2,3,4,5,6))


def print_kwargs(**kwargs):
    for k, val in kwargs.items():
        print(k, val)
print_kwargs(a=1, b=2, c=3)

def print_kwargs(**kwargs):
    for keyword, val in kwargs.items():
        print(keyword, val)
    for i, j in kwargs.items():
        print(i, j)
print_kwargs(len= 10, breath=22, height=33)