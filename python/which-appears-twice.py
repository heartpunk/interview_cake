import random

from hypothesis import given
import hypothesis.strategies as st



def which_appears_twice(numbers):
    def prod(multiplicands):
        return reduce(lambda x, y: x * y, multiplicands, 1)

    prod_numbers = prod(numbers)
    our_range = range(1, max(numbers) + 1)
    prod_range = prod(our_range)

    return prod_numbers / prod_range

@given(st.integers(min_value=2), st.integers(min_value=0))
def test_which_appears_twice(top_number, expected_number):
    modulo_base = (top_number - 1)
    modified_expected_number = (expected_number % modulo_base) + 1
    assert modified_expected_number <= top_number
    assert modified_expected_number != 0

    if modified_expected_number == 1:
        return
    expected_number = modified_expected_number

    numbers = range(1, top_number)
    numbers += [expected_number]

    assert expected_number in numbers
    assert len(numbers) == len(set(numbers)) + 1

    if __debug__:
        result = which_appears_twice(numbers)
        print "main", top_number, expected_number, numbers, result, expected_number

    assert which_appears_twice(numbers) == expected_number

test_which_appears_twice()
