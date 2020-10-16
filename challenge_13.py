# ask user to make a sentence
sentence = input("Please enter a sentence: ")
# ask user for the word that they what to replace
old = input("Please enter the word you want to replace: ")
# and replace the chosen word with the word that the user chose
new = input("What word would you like to replace it with? ")

# look at the error...
# it doesn't like "with"
# go back and read how to use replace in the docs
new_sentance = sentence.replace(old, new)

# test it out
# print new sentence
print(new_sentance)
