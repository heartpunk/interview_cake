from hypothesis import given
import hypothesis.strategies as st

# their example tree class
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

def all_paths(tree):
    to_visit = [tree]
    path = []

    while to_visit:
        current = to_visit.pop()

        if current in path:
            path = path[:path.index(current)]
        else:
            path.append(current)

        children = filter(None, [current.left, current.right])
        to_visit.extend(children)

        if not children:
            yield path

def is_superbalanced(tree):
    return len(map(len, set(all_paths(tree)))) in (0,1)

@given(st.integers(), st.lists(st.tuples(st.lists(st.integers(min_value=0, max_value=1)), st.integers())))
def some_random_trees(initial_value, inserts):
    def process_direction(local_tree, direction, value):
        assert direction in (0,1)

        direction = "left" if direction == 0 else "right"

        if getattr(local_tree, direction):
            return getattr(local_tree, direction)
        else:
            return getattr(local_tree, "insert_%s" % direction)(value)

    tree = BinaryTreeNode(initial_value)

    # 0 is left, 1 is right.
    for directions, value in inserts:
        sub_tree = tree
        for direction in directions:
            sub_tree = process_direction(sub_tree, direction, value)

    print(map(len, all_paths(tree)))

some_random_trees()
