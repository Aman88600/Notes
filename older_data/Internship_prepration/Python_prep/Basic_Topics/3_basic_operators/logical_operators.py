# Logical operators like and or not

a = 10
b = 12
c = 10
if (a > b) or (b > a):
    print("or works")

if (a < b) and (a == c):
    print("and works")

if not(a==b):
    print("not works")    