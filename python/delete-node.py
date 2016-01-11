# their linked list implementation.
class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None

a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c
# end their code

def delete(node):
    node.value = node.next.value
    node.next = node.next.next

delete(b)
