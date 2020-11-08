# Where is challenge 27?

# ask user for 5 names
import random
# print random name

# each of the below assignments will overwrite the other
# you need a unique assignment for each name

# you need to add each name to a list, so define the list first
# use the 'append()' method to add names to a list https://www.w3schools.com/python/ref_list_append.asp

name = input("please enter a name: ")
name = input("Please enter another name: ")
name = input("Please enter another name: ")
name = input("Please enter another name: ")
name = input("Please enter another name: ")

# read above comments about this line
mylist = [name]

# this is correct if you list has been populated correctly
computer_choice = random.choice(mylist)

msg = "The computer choice is {}"

# this is incorrect, as you are printing the list, not the choice
print(msg.format(mylist))
