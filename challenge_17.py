# print odd num only
# 4 is incorrect below, as you will skip some odd numbers
for num in range(1, 100, 4):
    print(num)

# a better approach is to learn about modulus
# read this: https://www.freecodecamp.org/news/the-python-modulo-operator-what-does-the-symbol-mean-in-python-solved/

# Modulus is an operator like +, -, *, and /, but will result in the remainder of a division operation.

# When you divide an even number by two, the result of the modulus operation will always be 0.

# Therefore:
# if
x = 100 % 2
print(x)
# x will be 0
# However:
# if
x = 101 % 2
print(x)
# x will not equal 0

# Your program should use the following logic:
# Run through a range of numbers
# For each number, check if it is even by using the modulus operator
# If the modulus is zero, print the number; otherwise do not print the number