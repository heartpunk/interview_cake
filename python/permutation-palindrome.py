from collections import Counter

def permutation_palindrome_checker(string):
    meta_counts = Counter(count for item, count in Counter(string).items()).items()

    for item, count in meta_counts:
        if item == 1:
            if count != 1:
                return False
        elif item % 2 != 0:
            return False

    return True

assert permutation_palindrome_checker("civic") is True
assert permutation_palindrome_checker("ivicc") is True
assert permutation_palindrome_checker("civil") is False
assert permutation_palindrome_checker("livci") is False
