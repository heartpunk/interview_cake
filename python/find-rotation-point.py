from hypothesis import given
import hypothesis.strategies as st

def find_rotation_point(items):
    min_index = 0
    max_index = len(items) - 1

    if items[min_index] < items[max_index]:
        return 0

    while min_index + 1 < max_index:
        pivot = ((max_index - min_index) / 2) + min_index

        assert not ((pivot < items[max_index]) and (pivot > items[min_index]))

        if items[pivot] > items[max_index]:
            min_index = pivot
        elif items[pivot] < items[min_index]:
            max_index = pivot

    return max_index

@given(st.integers(), st.sets(st.integers(), min_size=2))
def find_rotation_point_acts_sensibly(rotation_point, ints):
    rotation_point = rotation_point % len(ints)

    rotated_ints = sorted(list(ints))
    new_rotation_point = len(rotated_ints[rotation_point:]) % len(ints)
    rotated_ints = rotated_ints[rotation_point:] + rotated_ints[:rotation_point]

    assert find_rotation_point(rotated_ints) == new_rotation_point

find_rotation_point_acts_sensibly()

words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote', # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

print find_rotation_point(words)
