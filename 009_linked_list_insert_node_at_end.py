class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_ll(head):
    current = head
    while current:
        print(current.val, end=' -> ')
        current = current.next
    print('None')
    
def insert_node_at_end(head, val):
    current = head
    if not current:
        return head
    while current.next:
        current = current.next
    current.next = Node(val)
    return head

prime_numbers = Node(2)
prime_numbers = insert_node_at_end(prime_numbers, 3)
prime_numbers = insert_node_at_end(prime_numbers, 5)
prime_numbers = insert_node_at_end(prime_numbers, 7)
prime_numbers = insert_node_at_end(prime_numbers, 11)
prime_numbers = insert_node_at_end(prime_numbers, 13)
prime_numbers = insert_node_at_end(prime_numbers, 17)
prime_numbers = insert_node_at_end(prime_numbers, 19)

print_ll(prime_numbers)