x = int(input("Please enter a number: "))
y = int(input("Please enter another number : "))
q = x / y
# What type is q?
print(type(q))
# q is a float!
msg = "The quotient of {} / {} is {}"
print(msg.format(x, y, q))
