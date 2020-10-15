str = "Hail to the chief! Hail Hail Hail!"
words = str.split()
print("List", words)

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

# dictionary = {
# "Hail": 3,
# "to": 1,
# "the": 1,
# "chief!": 1,
# "Hail!: 1"
# }

print("Dictionary: ", word_count(str))