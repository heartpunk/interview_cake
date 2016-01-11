class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next  = None

    def __str__(self):
        next = self
        ret = []

        while next:
            ret.append(next.value)
            next = next.next

        return str(ret)

a =          LinkedListNode(1)
b = a.next = LinkedListNode(2)
c = b.next = LinkedListNode(3)
d = c.next = LinkedListNode(4)
e = d.next = LinkedListNode(5)

a1 = LinkedListNode(1)

def reverse(node):
    last = None

    while node.next:
        next = node.next
        node.next = last
        last = node
        node = next

    node.next = last
    return node

print a, b, c, d, e
print reverse(a)
print a, b, c, d, e

print a1
print reverse(a1)
print a1
