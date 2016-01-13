import collections
import random

def rand7():
    return random.randint(1,7)

def rand5():
    num = rand7()

    while num > 5:
        num = rand7()

    return num

print sorted(collections.Counter(rand5() for _ in range(50000)).items())
