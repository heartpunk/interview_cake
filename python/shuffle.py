import collections
import random

def our_shuffle(input):
    indices = range(len(input))

    output = [None] * len(input)

    for i in xrange(len(input)):
        rand_num = random.randint(0, len(indices) - 1)
        random_index = indices[rand_num]
        indices = indices[:rand_num] + indices[rand_num + 1:]
        output[i] = input[random_index]

    return output

def our_in_place_shuffle(input):
    for i in xrange(len(input) - 1):
        random_index = random.randint(i + 1, len(input) - 1)
        input[i], input[random_index] = input[random_index], input[i]

    return input


seq_length = 10
position_counters = [collections.Counter() for _ in range(seq_length)]

for _ in range(5000):
    shuffled = our_in_place_shuffle(range(seq_length))

    for index, value in enumerate(shuffled):
        position_counters[index].update([value])

print "if the second column of the following table all shows low and similar values, the output is likely random.\n"

for position, counter in enumerate(position_counters):
    def mean(nums):
        return sum(nums) / len(nums)

    dist = map(lambda x: x[1], sorted(counter.items(), lambda a, b: a[0] < b[0]))
    variance = max([x-mean(dist) for x in dist])
    print position, variance, dist
