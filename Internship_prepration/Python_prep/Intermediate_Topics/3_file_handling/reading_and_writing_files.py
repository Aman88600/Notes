file = open("names.txt", "w")
file.write("Aman Basoya")
file.close()

file = open("names.txt", "r")
text = file.read()
print(text)
file.close()

file = open("names.txt", "a+")
file.write(" Hello, World!")
file.close()

file = open("names.txt", "r")
text = file.read()
print(text)
file.close()