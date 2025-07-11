from collections import deque

# Stack, is first in last out
stack = deque()

stack.append("Aman")
stack.append("Nikhil")
stack.append("Mukund")

print(stack)

print(stack.pop())
print(stack)


# Queue is First in First out!
print("\nQueue Starts from here!")
queue = deque()

queue.append("Aman")
queue.append("Nikhil")
print(queue)
queue.popleft()
print(queue)


# Linked List
print("\nLinked List starts here!")

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None






def push(node):
    global head
    if head == None:
        head = node
    elif not(head == None):
        ptr = head
        while not(ptr.next==None):
            ptr = ptr.next
        ptr.next = node

# Head defined
head = None



def peek():
    global head

    if (head == None):
        print("List is Empty!")
    elif not(head==None):
        ptr = head
        while not(ptr==None):
            print(f"{ptr.value}")
            ptr = ptr.next


def delete_node():
    global head
    if (head == None):
        print("List is Empty!")
    elif not(head == None):
        ptr = head
        ptr2 = ptr.next
        while not(ptr2.next==None):
            ptr = ptr.next
            ptr2 = ptr.next
        ptr.next = None


while True:
    user_input = int(input("\nPress 1 to Add\n2 to peek\n3 to delete the last node\n"))
    if user_input == 1:
        value = int(input("Enter Node value:"))
        node = Node(value)
        push(node)
    elif user_input == 2:
        print("Current List")
        peek()
    elif user_input == 3:
        delete_node()
    else:
        break