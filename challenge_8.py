# write program to change munber into grades

# "Please enter a number" is better
num = input("type down a number:")

# This section doesn't make sense
'a' >= 75
'b' >= 60
'c' >= 35
'd' <= 35
# 

# instead of a, b, c, d, do the following
# if num >= 75:
#     print("A")

# fix the below

if 'a' == num:
    print("A")
else:
    print("B")
if 'b' == num:
    print("B")
else:
    print("c")
if 'c' == num:
    print("C")
else:
    print("D")
if 'd' == num:
    print("D")
else:
    print("F")
