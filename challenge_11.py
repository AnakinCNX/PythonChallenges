# ask user to input sentence
sentence = input("Please enter a sentence: ")
# calculate how many word there are

def word_count(str):
    words = str.split()
    return len(words)

numberOfWords = word_count(sentence)
# print the result
print(numberOfWords)
