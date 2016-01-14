def linear_egg_search(breaks, min=1, max=100, drops = 0):
    for floor in range(min,max+1):
        print floor, drops
        drops += 1

        if breaks(floor):
            return (floor - 1, drops)

def binary_egg_search(breaks):
    max = 100
    min = 1
    egg_count = 2
    drops = 0

    while egg_count and min < max:
        mid = min + (max-min)/2
        print min, max, mid, drops
        last_vals = [max, min, egg_count, mid]

        if egg_count == 2:
            drops += 1
            if breaks(mid):
                egg_count -= 1
                max = mid
            else:
                if min == mid:
                    min = max
                else:
                    min = mid
        else:
            print "entering exhaustive search"
            floor, drops = linear_egg_search(breaks, min, max, drops)
            min = max = floor # trigger loop exit


        if last_vals == [max, min, egg_count, mid]:
            print "fuck we're in a loop"
            break

    return (min, drops)

def exponential_egg_search(breaks):
    egg_count = 2
    drops = 0
    min = 1
    max = 100

    for floor in (2**n for n in range(100) if 1 < 2**n <= 100):
        drops += 1
        if breaks(floor):
            egg_count -= 1
            max = floor
            break
        else:
            min = floor

    floor, drops = linear_egg_search(breaks, min, max, drops)

    return (floor - 1, drops)

# need this to avoid python weirdness in the list comprehension below
def curried_egg_search(divisions):
    return lambda breaks: even_egg_search(breaks, divisions)

def even_egg_search(breaks, divisions):
    floors_to_try = range(1, 101, 100/divisions)[1:]
    egg_count = 2
    drops = 0
    min = 1
    print "floors to try", floors_to_try

    for floor in floors_to_try:
        print floor, drops
        drops += 1
        if breaks(floor):
            egg_count -= 1
            print "main"
            print "entering exhaustive search", min, floor, drops
            return linear_egg_search(breaks, min, floor, drops)
        else:
            min = floor + 1

    print "fallback"
    print "entering exhaustive search", min, 100, drops
    return linear_egg_search(breaks, min, 100, drops)

egg_searches = [
        #["linear", linear_egg_search],
        ["binary", binary_egg_search],
        ["exponential", exponential_egg_search],
]

egg_searches += [["even_egg_search %i divisions" % n, curried_egg_search(n)] for n in range(2, 30)]

def test_egg_searches():
    drops_by_name = {name: [] for name, _ in egg_searches}

    for i in range(2,100):
        for name, function in egg_searches:
            print name, "egg search for i =", i
            ret, drops = function(lambda x: x>i)
            print "result is", ret, "drop count is", drops, "for", name

            drops_by_name[name].append(drops)

    print ""
    for name, drops in sorted(drops_by_name.items(), key=lambda a: a[0]):
        print name, sum(drops)/len(drops), max(drops), "\n\t", drops


test_egg_searches()
