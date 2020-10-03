int num1 = input("Please enter a number: ")
# This shows the type of num1
print(type(num1))
int num2 = input("Please enter another number: ")

avg = (num1 + num2) / 2

message = "The average of {} and {} is {}"
print(message.format(num1, num2, int(avg)))