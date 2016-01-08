# their binary tree class
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right
# end their code

def check_ordering_property(tree):
    to_visit = [(None, None, tree)]

    while to_visit:
        min_value, max_value, current = to_visit.pop()

        if ((max_value and current.value >= max_value) or
            (min_value and current.value <= min_value)):
            return False

        if current.left:
            current.to_visit.append((min_value, current.current.value, current.left))

        if current.right:
            current.to_visit.append((current.current.value, max_value, current.right))

    return True
