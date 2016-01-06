meetings = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

def by_sorting(ranges):
    def overlaps(first, second):
        assert first[0] < first[1]
        assert second[0] < second[1]

        def core(x, y):
            return x[1] >= y[0] and x[0] < y[1]

        return core(first, second) or core(second, first)

    def merge_ranges(first, second):
        return (min(first[0], second[0]), max(first[1], second[1]))

    ranges = sorted(ranges)
    condensed_ranges = []
    open_range = (-2,-1)

    for candidate_range in ranges:
        if overlaps(candidate_range, open_range):
            open_range = merge_ranges(candidate_range, open_range)
        else:
            if open_range != (-2,-1):
                condensed_ranges.append(open_range)
            open_range = candidate_range

    return condensed_ranges + [open_range]

def condense_meeting_times(times):
    return by_sorting(times)

print condense_meeting_times(meetings)
print condense_meeting_times([(1, 2), (2, 3)])
print condense_meeting_times([(1, 5), (2, 3)])
print condense_meeting_times([(1, 10), (2, 6), (3, 5), (7, 9)])
