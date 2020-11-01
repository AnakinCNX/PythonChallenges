# ask user for 5 names
import random
# print random name

name = input("please enter a name: ")
name = input("Please enter another name: ")
name = input("Please enter another name: ")
name = input("Please enter another name: ")
name = input("Please enter another name: ")

mylist = [name]
computer_choice = random.choice(mylist)
msg = "The computer choice is {}"


print(msg.format(mylist))
