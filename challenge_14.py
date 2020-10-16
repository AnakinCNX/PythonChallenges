# ask user for sentence
sentence = input("Please type down a sentence: ").lower()

# are you missing an input?
# no:  "the" will be "hard-coded"

# create list from sentance
# what method creates a list from a string?
list = sentence.split()

# count how many times the word, "the" is in the sentance!

the_the_counter = sentence.count("the")

# what method can I use on list to count the word "the" ????


# print how many times a word occurs
print(the_the_counter)
