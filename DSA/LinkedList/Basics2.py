class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,val):
        new_node=Node(val)

        # if the list is empty we initialise it with the first node 
        if self.head is None:
            self.head=new_node
            return 
        

        current=self.head
        while current.next is not None:
            current=current.next

        current.next=new_node
    
    def display(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
        print("None")

ll=LinkedList()

ll.append(13)
ll.append(27)
ll.append(35)

ll.display()
    
        

    