class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def print_ll(head):
    current = head
    while(current):
        print(current.val, end=' -> ')
        current = current.next
    print('None')
    
def insert_node_at_specific_place(head, target_val, val):
    if head is None:
        return(None)
    
    current = head
    while(current and current.val != target_val):
            current = current.next

    if current:
        new_node = Node(val)
        new_node.next = current.next
        current.next = new_node
    return(head)

def reverse_iteratively(head):
    if head == None or head.next==None:
        return(head)
    current = head
    prev = None
    while(current):
        next = current.next
        current.next = prev
        prev = current
        current = next
    return(prev)

def reverse_recursively(head):
    if head is None or head.next is None:
        return(head);
    new_head = reverse_recursively(head.next)
    head.next.next = head
    head.next = None
    return(new_head)

prime_numbers = Node(2)
insert_node_at_specific_place(prime_numbers, 2, 3)
insert_node_at_specific_place(prime_numbers, 3, 5)
insert_node_at_specific_place(prime_numbers, 5, 7)
insert_node_at_specific_place(prime_numbers, 7, 11)
insert_node_at_specific_place(prime_numbers, 11, 13)
print('Prime numbers:')
print_ll(prime_numbers)

prime_numbers = reverse_iteratively(prime_numbers);
print('\n\n Reversed iteratively:')
print_ll(prime_numbers)

prime_numbers = reverse_recursively(prime_numbers);
print('\n\n Reversed the reverse, recursively:')
print_ll(prime_numbers)