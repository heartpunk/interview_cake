"""
This whole file implements the solution to the wrong thing. It's a fine solution,
but instead of addressing riffle as it is actually defined, it checks if something is
what we'll call a "perfect riffle", which is where two halves are exactly the same length,
and interspersed perfectly. For an example, imagine we have first_half and second_half, and
both are 2 items long. A perfect riffle of these would be either of :

[first_half[0], second_half[0], first_half[1], second_half[1]]
[second_half[0], first_half[0], second_half[1], first_half[1]]

So, while this code is correct, I'll have to redo this one later, once I've hopefully
forgotten more of the solution.
"""

def single_riffle_check_memory_inefficient(maybe_riffled, first_half, second_half):
    pairs = zip(first_half, second_half)

    return maybe_riffled in (
        reduce(lambda a, b: a + [b[0], b[1]], pairs),
        reduce(lambda a, b: a + [b[1], b[0]], pairs)
    )

def single_riffle_check(maybe_riffled, first_half, second_half):
    halves = (first_half, second_half)
    if maybe_riffled[0] == first_half[0]:
        offset = 0
    elif maybe_riffled[0] == second_half[0]:
        offset = 1
    else:
        return False

    for index in range(len(maybe_riffled)):
        halves_index = (index + offset) % 2
        if maybe_riffled[index] != halves[halves_index][index / 2]:
            return False

    return True

examples = [
    [[range(53), range(0, 53, 2), range(1, 53, 2)], True],
    [[range(53), range(1, 53, 2), range(0, 53, 2)], True],
    [[range(52, 0, -1), range(52, 0, -2), range(51, 0, -2)], True],
    [[range(52, 0, -1), range(51, 0, -2), range(52, 0, -2)], True],
]

from pprint import pprint
#pprint(examples)

for args, outcome in examples:
    assert single_riffle_check(*args) is outcome
