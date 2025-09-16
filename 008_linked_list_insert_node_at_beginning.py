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

def insert_node_at_beginning(head, val):
    node = Node(val)
    node.next = head
    return node

        

prime_numbers = None
prime_numbers = insert_node_at_beginning(prime_numbers, 2)
prime_numbers = insert_node_at_beginning(prime_numbers, 3)
prime_numbers = insert_node_at_beginning(prime_numbers, 5)
prime_numbers = insert_node_at_beginning(prime_numbers, 7)
prime_numbers = insert_node_at_beginning(prime_numbers, 11)

print_ll(prime_numbers)

    
    
    
    
    
    