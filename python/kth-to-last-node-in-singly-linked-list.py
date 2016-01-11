import collections

def kth_to_last_node(k, start):
    node = start
    buffer = collections.deque()

    while node:
        buffer.appendleft(node)
        if len(buffer) == k + 1: buffer.pop()
        node = node.next

    if len(buffer) == k: return buffer[-1]


# begin their code
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next  = None

a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

print kth_to_last_node(2, a).value
# returns the node with value "Devil's Food" (the 2nd to last node)
