
'''reverse a linked list

2 (200) -> 4(400) -> 8(500) -> 16(None)'''

class linkedList:
    def __init__(self):
        self.head = None
        
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next
    
    def reversalList(self):
        prev = None
        curr = self.head
    
        while curr:
            next_ptr = curr.next
            curr.next = prev
            prev = curr
            curr = next_ptr
        
        # linkage of head node to the last node is required
        self.head = prev
    
    def printList(self):
        curr = self.head
        while curr:
            print(f"{curr.data} -> ", end="")
            curr = curr.next
        print("None")
        
ll = linkedList()
ll.head = linkedList.Node(2)
ll.head.next = linkedList.Node(4)
ll.head.next.next = linkedList.Node(8)
ll.head.next.next.next = linkedList.Node(16)
ll.head.next.next.next.next = linkedList.Node(32)
ll.head.next.next.next.next.next = linkedList.Node(64)

print("original linked list")
ll.printList()

print("reversal linked list")
ll.reversalList()
ll.printList()