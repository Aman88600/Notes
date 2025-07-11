# Lists are like arrays, Ordered, Changeable, Allow Duplicates, Can contain different datatypes

numbers = [i for i in range(10)]
print(numbers)
# Access list item
print(numbers[2])
# Chnage list item
numbers[2] = "Hello"
print(numbers)
# Chnage a range of items
numbers[1:3] = ["hello", "World"]
print(numbers)

# Insert function, here the items will not be replaced by the given item, the list will become bigger
numbers.insert(1, "Aman") # position, item
print(numbers)

# Append
numbers.append("Orange")
print(numbers)