class ListNode:
    def __init__(self,val):
        self.data=val
        self.next=None

l1=ListNode(13)
l2=ListNode(18)
l3=ListNode(25)
l4=ListNode(67)



l1.next=l2
l2.next=l3
l3.next=l4

head=l1


def removeNthnode(head,n):

    dummy=ListNode(0)
    dummy.next=head
    slow=fast=dummy

    for _ in range(n):
        fast=fast.next


    while fast.next is not None:
        slow=slow.next
        fast=fast.next

    slow.next=slow.next.next
    return dummy.next


new_head=removeNthnode(head,2)
current=new_head
while current:
    print(current.data,end="->")
    current=current.next
print("None")
