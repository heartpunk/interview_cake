# their binary tree
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

def second_largest_item_in_bst(tree):
    def largest_and_parent(subtree):
        while tree.right:
            last_node = tree
            tree = tree.right

        return (tree, last_node)

    tree, parent = largest_and_parent(tree)

    if tree.left:
        return largest_and_parent(tree.left)[0].value
    else:
        return parent.value
