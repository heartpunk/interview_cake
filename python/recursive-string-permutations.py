import itertools
import string

from hypothesis import given
import hypothesis.strategies as st



def our_permutations(string, used_indices=None):
    if used_indices is None:
        used_indices = []

    assert len(used_indices) <= len(string)

    if len(used_indices) == len(string):
        return ''.join(string[index] for index in used_indices)
    else:
        used_indices_set = set(used_indices)
        ret = [our_permutations(string, used_indices=used_indices + [index]) for index in range(len(string)) if index not in used_indices_set]

        if type(ret[0]) == str:
            return ret
        else:
            return reduce(lambda x, y: x + y, ret)

@given(st.lists(st.sampled_from(string.printable), min_size = 1, max_size=5))
def test_permutations_against_built_in(string):
    string = ''.join(string)

    ours = our_permutations(string)
    theirs = list(''.join(permutation) for permutation in itertools.permutations(string))

    if __debug__:
        print repr(string), repr(ours), theirs

    assert id(ours) != id(theirs)
    assert ours == theirs

test_permutations_against_built_in()
