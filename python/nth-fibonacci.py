def fib(n):
    last = 0
    current = 1

    if n == 0:
        return last
    elif n == 1:
        return current

    for i in range(n - 1):
        tmp = last + current
        last = current
        current = tmp

    return current

print map(fib, range(10))
