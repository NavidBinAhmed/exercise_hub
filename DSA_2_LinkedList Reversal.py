
'''reverse a linked list

2 (200) -> 4(400) -> 8(500) -> 16(None)'''


def reversalList(self):
    prev = None
    next_ptr = None
    curr = self.head
    
    while curr:
        next_ptr = curr.next
        curr.next - prev
        prev = curr
        curr = next_ptr
    
    # linkage of head node to the last node is required
    self.head = prev 
    
    print("original linked list")
    print("reversal linked list")
    result = reversalList(self)
    print(result)