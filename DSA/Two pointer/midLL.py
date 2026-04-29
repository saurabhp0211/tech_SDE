class LinkNode:
    def __init__(self,val):
        self.data=val
        self.next=None

h0=LinkNode(12)
h1=LinkNode(20)
h2=LinkNode(36)
h3=LinkNode(42)
h4=LinkNode(48)

h0.next=h1
h1.next=h2
h2.next=h3
h3.next=h4


current=h0
count=0
while current is not None:
    count+=1
    print(current.data,end="->")
    current=current.next
print("None")
print(count)


head=h0
def middleOfLL(head):
    slow=fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    return slow

middleofLinkedList=middleOfLL(head)
print(f"the middle of the linked list is {middleofLinkedList.data}")

