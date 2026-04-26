class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

node1=Node(10)
node2=Node(84)
node3=Node(9)

node1.next=node2
node2.next=node3

head=node1
current=head

while current is not None:
    print(current.data, end=" -> ")
    current=current.next
print("None")
