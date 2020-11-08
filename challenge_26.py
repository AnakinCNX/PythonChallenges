name = input("Please enter your name: ")
# Ask user for name for quiz
# ask user for the answers for the quiz

# Don't use a capital letter when assigning variables.
Q1 = input("What is 3+2: ")

# You need to write this so that the user is:
#  1) presented with a question
#  2) given the chance to respond
#  3) is asked the next question

#  You can either tell them if each answer is right or wrong, or better
#  You can keep track of the score, and at the end of the quiz, give them a total score.

# Pay attention to types, because you can't do math with strings.

if Q1 == 5:
    print("correct")
else:
    print("incorrect")

Q2 = input("what is 25*4: ")


if Q2 == 100:
    print("correct")
else:
    print("incorrect")

Q3 = input("what is 100/10: ")


if Q3 == 10:
    print("correct")
else:
    print("incorrect")
