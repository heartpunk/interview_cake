def find_matching_paren(string, paren_index):
    count = 0

    for index in range(paren_index, len(string)):
        if string[index] == "(":
            count += 1

        if string[index] == ")":
            count -= 1

            if count == 0:
                return index

assert find_matching_paren("Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing.", 10) == 79
