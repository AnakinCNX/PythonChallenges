# Make user play rock paper scissors with computer
import random

mylist = ["rock", "paper", "scissors"]

def get_user_input():
    users_choice = input("Rock, paper or scissors?: ").lower()
    return users_choice
    
users_choice = get_user_input()

while users_choice not in mylist:
    print("Invalid input!  Please try again.")
    users_choice = get_user_input()

computers_choice = random.choice(mylist)
msg = "The computer chose {}"

def get_game_result():
    result = ""
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
    return result

game_result = get_game_result()
print(game_result)
