import string

from hypothesis import given
import hypothesis.strategies as st



def reverse_string(string):
    string_as_list = [char for char in string]

    for i in range(len(string_as_list)):
        tmp = string_as_list[i]
        string_as_list[i] = string_as_list[-(i+1)]
        string_as_list[-(i+1)] = tmp

    return ('').join(string_as_list)

@given(st.lists(st.sampled_from(string.printable)))
def test_reverse_string(chars):
    string = ('').join(chars)
    reversed_string = reverse_string(string)
    double_reversed_string = reverse_string(reversed_string)

    if __debug__:
        print repr(string), repr(reversed_string), repr(double_reversed_string)

    assert string == double_reversed_string

test_reverse_string()
