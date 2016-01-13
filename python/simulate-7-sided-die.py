import collections
import random

def rand5():
    return random.randint(1,5)

def rand7():
    while True:
        ret = 10
        roll1 = rand5()
        roll2 = rand5()
        roll3 = rand5()

        if roll1 > 2 or roll2 > 2:
            next

        if roll1 == 1:
            ret = roll3
        elif roll1 == 2:
            ret = 5 + roll2
        if ret <= 7:
            return ret


print sorted(collections.Counter(rand7() for _ in range(500000)).items())
