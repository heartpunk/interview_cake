import collections

from hypothesis import given
import hypothesis.strategies as st



class queue_from_stacks(object):
    def __init__(self):
        self._left = []
        self._right = []

    def enqueue(self, value):
        self._left.append(value)

    def dequeue(self):
        if not self._right and self._left:
            self._right.extend(reversed(self._left))
            self._left = []

        return self._right.pop()

@given(st.lists(st.tuples(st.sampled_from(("pop", "push")), st.integers())))
def test_queue_from_stacks(operations):
    our_queue = queue_from_stacks()
    python_queue = collections.deque()

    for operation, value in operations:
        assert operation in ("pop, push")

        if operation == "pop" and len(python_queue):
            our_pop = our_queue.dequeue()
            python_pop = python_queue.pop()

            if __debug__:
                print our_pop, python_pop

            assert our_pop == python_pop
        elif operation == "push":
            our_queue.enqueue(value)
            python_queue.appendleft(value)

test_queue_from_stacks()
