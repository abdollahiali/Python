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

prime_numbers = Node(2)
insert_node_at_specific_place(prime_numbers, 2, 3)
insert_node_at_specific_place(prime_numbers, 3, 5)
insert_node_at_specific_place(prime_numbers, 5, 11)
insert_node_at_specific_place(prime_numbers, 11, 13)
print('Initial prime numbers list with number 7 missing:')
print_ll(prime_numbers)
insert_node_at_specific_place(prime_numbers, 5, 7)
print('\nInsering number 7 after number 5:')
print_ll(prime_numbers)
