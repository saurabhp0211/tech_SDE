class Listnode:
    def __init__(self,x):
        self.val=x
        self.next=None

l1=Listnode(3)
l2=Listnode(6)
l3=Listnode(9)
l4=Listnode(12)

l1.next=l2
l2.next=l3
l3.next=l4

# creates a cycle
l4.next=l2

head=l1

def hasCycle(head):
    slow=fast=head
    
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return True
    return False

print(f"Cycle detected : {hasCycle(head)}")