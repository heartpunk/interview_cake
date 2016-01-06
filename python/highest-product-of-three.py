import heapq
import sys

bound = 10**int(sys.argv[1])

if len(sys.argv) > 2:
    from random import randint
    list_of_ints = [randint(-sys.maxint - 1, sys.maxint) for i in xrange(-bound, bound)]
else:
    list_of_ints = list(xrange(-bound, bound))

def prod(nums):
    return reduce(lambda x, y: x * y, nums, 1)

def heap_highest_product(ints):
    return prod(heapq.nlargest(3, ints, abs))

def highest_product(ints):
    def max_capacity_heap_push(capacity, heap, item, max_or_min="max"):
        if max_or_min == "min":
            _heapify = heapq._heapify_max
            _heappushpop = heapq._heappushpop_max
        elif max_or_min == "max":
            _heapify = heapq.heapify
            _heappushpop = heapq.heappushpop

        if len(heap) == capacity:
            _heappushpop(heap, num)
        else:
            assert len(heap) <= capacity
            heap.append(num)
            _heapify(heap)

    negatives = []
    positives = []

    for num in ints:
        if num < 0:
            max_capacity_heap_push(2, negatives, num, "min")
        else:
            max_capacity_heap_push(3, positives, num, "max")

    negatives = sorted(negatives)
    positives = sorted(positives)

    return max(prod(negatives) * positives[-1], prod(positives))

########## THEIR SOLUTION PASTED IN HERE FOR TESTING ###########
def highest_product_of_3(list_of_ints):
    if len(list_of_ints) < 3:
        raise Exception('Less than 3 items!')

    # We're going to start at the 3rd item (at index 2)
    # so pre-populate highests and lowests based on the first 2 items.
    # we could also start these as None and check below if they're set
    # but this is arguably cleaner
    highest = max(list_of_ints[0], list_of_ints[1])
    lowest =  min(list_of_ints[0], list_of_ints[1])

    highest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    lowest_product_of_2  = list_of_ints[0] * list_of_ints[1]

    # except this one--we pre-populate it for the first /3/ items.
    # this means in our first pass it'll check against itself, which is fine.
    highest_product_of_three = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    # walk through items, starting at index 2
    for current in list_of_ints[2:]:

        # do we have a new highest product of 3?
        # it's either the current highest,
        # or the current times the highest product of two
        # or the current times the lowest product of two
        highest_product_of_three = max(
            highest_product_of_three,
            current * highest_product_of_2,
            current * lowest_product_of_2)

        # do we have a new highest product of two?
        highest_product_of_2 = max(
            highest_product_of_2,
            current * highest,
            current * lowest)

        # do we have a new lowest product of two?
        lowest_product_of_2 = min(
            lowest_product_of_2,
            current * highest,
            current * lowest)

        # do we have a new highest?
        highest = max(highest, current)

        # do we have a new lowest?
        lowest = min(lowest, current)

    return highest_product_of_three
########## THEIR SOLUTION PASTED IN HERE FOR TESTING ###########

assert highest_product_of_3(list_of_ints) == highest_product(list_of_ints)
print highest_product(list_of_ints)
