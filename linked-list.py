class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


# Create three nodes
first = Node("Daniel")
second = Node("Mary")
third = Node("James")

# Link the nodes
first.next = second
second.next = third

# Traverse and print the list
current = first

while current is not None:
    print(current.data)
    current = current.next
