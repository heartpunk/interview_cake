from hypothesis import given
import hypothesis.strategies as st

def our_ways_of_making_change(amount, denominations):
    if all(map(lambda x: amount < x, denominations)):
        return 0

    change_for = [0] * (amount + 1)
    change_for[0] = 1

    for i in xrange(1, amount + 1):
        for coin in denominations:
            change_for[i] += change_for[i-coin]

    print change_for
    return change_for[amount]

def ways_of_making_change(amount, denominations):
    change_for = [0] * (amount + 1)
    change_for[0] = 1

    for coin in denominations:
        for i in xrange(coin, amount + 1):
            change_for[i] += change_for[i-coin]

    print change_for
    return change_for[amount]

@given(st.integers(min_value=0), st.lists(st.integers(min_value=1), min_size=1))
def ours_works_like_theirs(amount, denominations):
    denominations = sorted(set(denominations))
    assert our_ways_of_making_change(amount, denominations) == ways_of_making_change(amount, denominations)

failing_cases = [
    [1, [2]],
    [1, [3]],
    [0, [1]]] # haha! found a bug in their code. =DDDD

for failing_case in failing_cases:
    ours = our_ways_of_making_change(*failing_case)
    theirs = ways_of_making_change(*failing_case)
    print ours, theirs, ours == theirs

ours_works_like_theirs()
