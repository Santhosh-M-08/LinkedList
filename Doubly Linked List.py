
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


head = None


# Add at beginning
def addFirst(val):
    global head

    node = Node(val)

    if head is None:
        head = node
    else:
        node.next = head
        head.prev = node
        head = node


# Add at end
def addLast(val):
    global head

    node = Node(val)

    if head is None:
        head = node
        return

    temp = head
    while temp.next is not None:
        temp = temp.next

    temp.next = node
    node.prev = temp


# Remove from beginning
def delFirst():
    global head

    if head is None:
        return

    if head.next is None:
        head = None
        return

    head = head.next
    head.prev = None


# Remove from end
def delLast():
    global head

    if head is None:
        return

    if head.next is None:
        head = None
        return

    temp = head
    while temp.next is not None:
        temp = temp.next

    temp.prev.next = None


# Add at a given position (1-based)
def addMiddle(val, pos):
    global head

    if pos < 1:
        print("Invalid position")
        return

    if pos == 1:
        addFirst(val)
        return

    temp = head

    for i in range(pos - 2):
        if temp is None:
            print("Invalid position")
            return
        temp = temp.next

    if temp is None:
        print("Invalid position")
        return

    node = Node(val)
    node.next = temp.next
    node.prev = temp

    if temp.next is not None:
        temp.next.prev = node

    temp.next = node


# Remove a node by value
def delMiddle(val):
    global head

    if head is None:
        return

    temp = head

    while temp is not None and temp.val != val:
        temp = temp.next

    if temp is None:
        print("Value not found")
        return

    if temp.prev is not None:
        temp.prev.next = temp.next
    else:
        head = temp.next

    if temp.next is not None:
        temp.next.prev = temp.prev


# Reverse the DLL
def reverse():
    global head

    temp = head
    prev_node = None

    while temp is not None:
        prev_node = temp.prev
        temp.prev = temp.next
        temp.next = prev_node
        head = temp
        temp = temp.prev


# Print forward
def display():
    temp = head

    while temp is not None:
        print(temp.val, end=" <-> ")
        temp = temp.next

    print("None")


# Test the operations
addLast(10)
addLast(20)
addLast(30)
addLast(40)

print("Original list:")
display()

addFirst(5)
print("After adding at first:")
display()

addLast(50)
print("After adding at last:")
display()

addMiddle(25, 5)
print("After adding 25 at position 5:")
display()

delFirst()
print("After removing first:")
display()

delLast()
print("After removing last:")
display()

delMiddle(25)
print("After removing value 25:")
display()

reverse()
print("After reversing:")
display()
