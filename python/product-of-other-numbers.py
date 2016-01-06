ints = [1,7,3,4]
partial_mults = {(): 1}
mults = []

def subsequences(seq):
    return [list(seq[:i-1] + seq[i:]) for i in range(1, len(seq) + 1)]

def product(seq):
    return reduce(lambda x, y: x * y, seq, 1)

def brute_force_get_products_of_all_ints_except_at_index(seq):
    return [product(sub_seq) for sub_seq in subsequences(seq)]

brute_force_get_products_of_all_ints_except_at_index(ints)

def too_much_space_usage_get_products_of_all_ints_except_at_index(seq):
    def compute_halves(seq):
        accumulator = 1
        for num in seq:
            accumulator *= num
            yield accumulator

    left_halves = list(compute_halves(seq))
    right_halves = list(reversed(list(compute_halves(reversed(seq)))))

    for i in xrange(len(seq)):
        if i == 0:
            prod = right_halves[1]
        elif i == len(seq) - 1:
            prod = left_halves[i - 1]
        else:
            prod = left_halves[i - 1] * right_halves[i + 1]

        print left_halves[i], right_halves[i], prod

def get_products_of_all_ints_except_at_index(seq):
    def populate_half(indices):
        accumulator = 1

        for i in indices:
            output[i] *= accumulator
            accumulator *= seq[i]

    output = [1] * len(seq)

    populate_half(xrange(len(seq)))
    populate_half(reversed(xrange(len(seq))))

    return output

print get_products_of_all_ints_except_at_index(ints)
