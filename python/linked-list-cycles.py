def detect_cycle(linked_list):
    turtle = linked_list
    hare = linked_list

    def hit_end(node):
        for i in range(4):
            if node is None:
                return True
            node = node.next
        return False

    while not (hit_end(turtle) or hit_end(hare)):
        turtle = turtle.next
        hare = hare.next.next

        if turtle == hare: return True

    return False
