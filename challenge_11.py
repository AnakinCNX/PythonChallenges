# ask user to input sentence
sentence = input("Please enter a sentence:")
# calculate how many word there are


def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


# print the result
print(word_count(sentence))
