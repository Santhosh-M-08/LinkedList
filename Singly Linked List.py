class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

head = None

#Adding Nodes
def addNode(val):
  global head
  if head==None:
    head = Node(val)
  else:
    temp = head
    while temp.next is not None:
      temp = temp.next
    temp.next=Node(val)

#Add First
def addFirst(val):
    global head
    node = Node(val)
    if head==None:
        head = node
    else:
        node.next = head
        head = node

#Add Last
def addLast(val):
  global head
  node = Node(val)
  if head == None:
    head = node
  else:
    temp = head
    while temp.next is not None:
      temp=temp.next
    temp.next=node

#Add Middle
def addMiddle(val,pos):
  global head
  node = Node(val)
  if pos == 1:
    addFirst(val)
  else:
    temp = head
    count = 0
    while count<pos-2 and temp is not None:
      count = count+1
      temp=temp.next
    node.next = temp.next
    temp.next = node

#Remove First
def delFirst():
    global head
    if head is not None:
        head=head.next

#Remove Last
def delLast():
    global head
    if head is None:
        return
    if head.next is None:
        head = None
    temp = head
    while temp.next.next is not None:
        temp=temp.next
    temp.next=None

#Remove Middle
def delmiddle(val):
  global head
  if head.val == val:
    head = head.next
  else:
    temp = head
    while temp is not None and temp.next.val!=val:
      temp=temp.next
    temp.next=temp.next.next

def reverse():
    global head

    prev = None
    temp = head

    while temp is not None:
        next_node = temp.next
        temp.next = prev
        prev = temp
        temp = next_node

    head = prev

n = int(input("Enter the number of nodes:"))
for i in range(n):
  val = int(input("Enter value:"))
  addNode(val)

#first = int(input(("Enter a value to add at first:")))
#addFirst(first)

#last = int(input("Enter a value to add at last:"))
#addLast(last)

#middle = int(input(("Enter a value to add at middle:")))
#pos = int(input("Enter the position"))
#addMiddle(middle,pos)

#delete = int(input("Enter a value to delete:"))
#delmiddle(delete)

#delFirst()
#delLast()

temp = head
while temp is not None:
    print(temp.val)
    temp=temp.next
