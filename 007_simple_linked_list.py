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
                

prime_numbers = Node(2)
prime_numbers.next = Node(3)
prime_numbers.next.next = Node(5)
prime_numbers.next.next.next = Node(7)
prime_numbers.next.next.next.next = Node(11)

print_ll(prime_numbers)

