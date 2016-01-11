from hypothesis import given
import hypothesis.strategies as st

# their stack class that we're meant to reuse
class Stack(object):

    # initialize an empty list
    def __init__(self):
        self.items = []

    # push a new item to the last index
    def push(self, item):
        self.items.append(item)

    # remove the last item
    def pop(self):
        # if the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items: return None

        return self.items.pop()

    # see what the last item is
    def peek(self):
        # if the stack is empty, return None
        if not self.items: return None

        return self.items[len(self.items)-1]
# end their code

class MaxStack(Stack):
    def __init__(self):
        super(self.__class__, self).__init__()
        self._max = sorted(self.items)

    def push(self, value):
        if self._max:
            if self.get_max() < value:
                self._max.append(value)
        else:
            self._max.append(value)
        super(self.__class__, self).push(value)

    def pop(self):
        ret = super(self.__class__, self).pop()

        if self._max and ret == self._max[-1]:
            self._max.pop()

        return ret

    def get_max(self):
        return self._max[-1] if self._max else None

@given(st.lists(st.tuples(st.sampled_from(("pop", "push")), st.integers())))
def test_max_stack(operations):
    max_stack = MaxStack()

    for operation, value in operations:
        assert operation in ("pop", "push")

        if operation == "pop":
            value = max_stack.pop()
            max = max_stack.get_max()

        else:
            max_stack.push(value)
            max = max_stack.get_max()

        if __debug__:
            print operation, value, max

test_max_stack()
