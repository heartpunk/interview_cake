import collections
import string

def word_cloud_data(text):
    def stripper(word):
        word = string.strip(word, '.:,?!?()')
        print word[-2:], word[:-2]
        if word[-2:] == "'s":
            print "yes!"
            word = word[:-2]
        return word.lower()

    def splitter(text):
        output = []
        buffer = []

        for char in text:
            if char == ' ':
                output.append(''.join(buffer))
                buffer = []
            else:
                buffer.append(char)
                if ''.join(buffer[-3:]) == "...":
                    buffer = buffer[:-3]

                    output.append(''.join(buffer))
                    buffer = []
        return output + [''.join(buffer)]

    return collections.Counter((stripper(word) for word in splitter(text)))

print word_cloud_data("We came, we saw, we conquered...then we ate Bill's (Mille-Feuille) cake.")
