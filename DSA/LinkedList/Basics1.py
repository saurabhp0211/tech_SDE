class Node:
    def __init__(self,val):
        self.data=val
        self.next=None



node1=Node(5)
node2=Node(10)
node3=Node(23)

node1.next=node2
node2.next=node3

head=node1
current=head
Tsum=0
while current is not None:
    print(current.data,end="->")
    Tsum+=current.data
    print(f"current sum :{Tsum}")
    current=current.next
    

print("None")