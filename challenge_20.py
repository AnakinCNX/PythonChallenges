# ask user for num and repeat until user got 7

# lists use [], not ()
# you don't need a list here, as you are only comparing one value (7)
# numlist = ("7") # don't use me

# you can just set 7 to be a variable, instead of a list.
# desired_number = "7"

num = int(input("Please enter a number: "))

# while num is not equal to 7
# keep asking for user input
while num != "7":
    print("Please try again")
# how to stop infinet loop?
if num == 7:
    print("well done")
# while loop breaks once user input equals 7

# say well done for getting the right number
