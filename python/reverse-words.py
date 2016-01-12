def reverse_words_sanely_but_not_in_place(string):
    return (' ').join(reversed(string.split(' ')))

def reverse_words_in_entirely_the_wrong_way(string):
    chars = [char for char in string]

    def write_word(index, word):
        for j, output_char in zip(range(index, index - len(word)), word):
            chars[j] = output_char

    current_word = []

    for i, input_char in enumerate(chars):
        if input_char == ' ':
            write_word(i, current_word)
            current_word = []
        else:
            current_word.append(input_char)

    write_word(len(chars) - 1, current_word)

    return ('').join(chars)

def reverse_words_inefficiently_and_not_actually_fully_implemented(string):
    chars = [char for char in string]

    end = len(chars)
    total_offset = 0

    word_indices = []

    print len(chars)

    for index, char in reversed(zip(range(len(chars)), chars)):
        if char == ' ':
            print index, end
            word_indices.append(((index, end), (total_offset, total_offset + (end - index))))
            total_offset += (end - index + 1)
            end = index

    word_indices.append((0, end))

    for index in word_indices:
        print index, ('').join(chars[index[0][0]:index[0][1]])

def reverse_words(string):
    chars = [char for char in string]

    def reverse_range_in_list(list, start, end):
        range_to_reverse = range(start, end)
        midway_point = (end-start)/2

        for left, right in zip(range_to_reverse[:midway_point], reversed(range_to_reverse[midway_point:])):
            chars[right], chars[left] = chars[left], chars[right]

    reverse_range_in_list(chars, 0, len(chars))

    start = 0
    for index in range(len(chars)):
        if chars[index] == ' ':
            reverse_range_in_list(chars, start, index)
            start = index + 1

    reverse_range_in_list(chars, start, len(chars))

    return ''.join(chars)


expected = 'if into the security recordings you go only pain will you find'
actual = reverse_words('find you will pain only go you recordings security the into if')

if __debug__:
    print "expected =", expected
    print "actual   =", actual

assert expected == actual
