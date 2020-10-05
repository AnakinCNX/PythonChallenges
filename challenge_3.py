# ask the user for the width and length of a shape
length = int(input("Please enter the length: "))
width = int(input("Please enter the width: "))
# calculate the area of the shape
area = length * width
# print the area of the shape
# Read the docs on Python String Formatting:
# https://www.w3schools.com/python/
# and/or look at examples in challenge 1
msg = "The area of the shape is {}"
# The arguments for the format method match the curly braces in msg
print(msg.format(area))
