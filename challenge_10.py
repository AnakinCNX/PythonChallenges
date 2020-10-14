# Make user play rock paper scissors with computer

import random
users_choice = input("Rock, paper or scissors?: ").lower()

mylist = ["rock", "paper", "scissors"]
computers_choice = random.choice(mylist)
msg = "The computer chose {}"

result = ""
if users_choice not in mylist:
    print("Invalid input!")
    exit()


if computers_choice == "rock" and users_choice == "rock":
    result = "It's a tie!"
elif computers_choice == "rock" and users_choice == "paper":
    result = "You won!"
elif computers_choice == "rock" and users_choice == "scissors":
    result = "Computer wins!"
elif computers_choice == "paper" and users_choice == "paper":
    result = "It's a tie!"
elif computers_choice == "paper" and users_choice == "rock":
    result = "Computer wins!"
elif computers_choice == "paper" and users_choice == "scissors":
    result = "You won!"
elif computers_choice == "scissors" and users_choice == "scissors":
    result = "It's a tie!"
elif computers_choice == "scissors" and users_choice == "paper":
    result = "Computer wins!"
elif computers_choice == "scissors" and users_choice == "rock":
    result = "You won!"
print(msg.format(computers_choice))
print(result)
