import collections
from hypothesis import given
import hypothesis.strategies as st

class TemperatureTracker(object):
    def __init__(self):
        self.counts = collections.Counter()
        self.min = float("inf")
        self.max = float("-inf")
        self._sum = 0
        self._count = 0
        self.mean = None
        self.mode = None

    def insert(self, value):
        self.min = min(self.min, value)
        self.max = max(self.max, value)
        self._sum += value
        self._count += 1
        self.mean = self._sum / self._count
        self.counts.update([value])
        if self.mode is None:
            self.mode = value
        elif self.counts[self.mode] < self.counts[value]:
            self.mode = value


@given(st.lists(st.integers(min_value=0, max_value=110), average_size=1000))
def temperature_tracker_does_not_fall_over(temps):
    tt = TemperatureTracker()

    print "=" * 75
    for temp in temps:
        tt.insert(temp)
        most_common = map(lambda x: x[0], tt.counts.most_common(1))
        import itertools
        all_counts = sorted(tt.counts.most_common(), lambda x, y: x[1] > y[1])
        dumb_mode = itertools.takewhile(lambda x: x[1] == all_counts[0][1], all_counts)
        dumb_mode = map(lambda x: x[0], dumb_mode)
        prints = ["inserted ", temp,
                  "\tmean is ", tt.mean,
                  "\tour mode is ", tt.mode,
                  "\treliable mode is ", tt.counts.most_common(1)[0][0],
                  "\tour mode is correct ", tt.mode in dumb_mode,
                  "\tmost common is ", most_common,
                  "\t counts is ", tt.counts,
                  "\t dumb_mode is ", dumb_mode,
                  "\tmin is ", tt.min,
                  "\tmax is ", tt.max
        ]
        print(''.join(map(str, prints)))

temperature_tracker_does_not_fall_over()
