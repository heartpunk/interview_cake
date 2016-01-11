import collections
import random

from hypothesis import given
import hypothesis.strategies as st



def find_unique_int_among_duplicates(confirmation_numbers):
    counter = collections.Counter()

    for confirmation_number in confirmation_numbers:
        counter[confirmation_number] += 1

    uniques = [confirmation_number for confirmation_number, count in counter.items() if count == 1]

    assert len(uniques) == 1

    return uniques[0]

@given(st.tuples(st.integers(), st.sets(st.integers())).filter(lambda x: x[0] not in x[1]))
def test_unique_int_finder(vals):
    unique, numbers = vals
    confirmation_numbers = []

    for number in numbers:
        confirmation_numbers.extend([number, number])

    confirmation_numbers.append(vals[0])
    random.shuffle(confirmation_numbers)

    found_unique = find_unique_int_among_duplicates(confirmation_numbers)
    print unique, found_unique

    assert unique == found_unique

test_unique_int_finder()
