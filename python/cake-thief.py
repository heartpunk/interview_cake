def max_duffel_bag_value(cake_tuples, capacity):
    max_values = [0] * (capacity + 1)

    if [() for weight, value in cake_tuples if weight == 0 and value > 0]:
        return float("inf")

    for sub_capacity in range(capacity + 1):
        for weight, value in cake_tuples:
            sub_solution_index = sub_capacity - weight
            if sub_solution_index >= 0: # negative indices wrap around in python!
                max_values[sub_capacity] = max(max_values[sub_solution_index] + value, max_values[sub_capacity])

    return max_values[capacity]

# their test code

cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity    = 20

print max_duffel_bag_value(cake_tuples, capacity)

# end their code

print max_duffel_bag_value(cake_tuples, 0)

ethereal_cake = (0, 1000)
print max_duffel_bag_value(cake_tuples + [ethereal_cake], 20)

worthless_ethereal_cake = (0, 0)
print max_duffel_bag_value(cake_tuples + [worthless_ethereal_cake], 20)
