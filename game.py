# Rock paper scissors
# User will enter their choice
# The program will randomly select Rock, paper, or scissors
# The score will be kept
# print results in a clean table

# rules: 
# rock[0] > scissor[2]
# paper[1] > rock[0]
# scissors[2] > paper[1]

import random

options = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

# call this method if the computer won the match
# print in table
def computer_won(current_computer_score):
    new_computer_score = current_computer_score + 1
    print()
    # found center align on pyformat.info
    print('{:^30}'.format('Results'))
    print()
    #print(computer_choice + " vs " + user_choice)
    print('{:5} {:13} {:10}'.format('', 'Computer', 'You'))
    print('{:5} {:13} {:10}'.format('', computer_choice, user_choice))
    print()
    print('{:^30}'.format("You lost"))
    print()
    print("Computer: " + str(new_computer_score) + "\tUser: " + str(user_score))
    print()
    return new_computer_score
# call this method if the user won the match
# print in a table
def user_won(current_user_score):
    new_user_score = current_user_score + 1
    print()
    print('{:^30}'.format('Results'))
    print()
    print('{:5} {:13} {:10}'.format('', 'Computer', 'You'))
    print('{:5} {:13} {:10}'.format('', computer_choice, user_choice))
    print()
    print('{:^30}'.format("You won!"))
    print()
    print("Computer: " + str(computer_score) + "\tUser: " + str(new_user_score))
    print()
    return new_user_score

# Summary
print("Beat the program!")

# loop so the user can play the game repeatedly 
while True:
    # Input from user
    user_choice = input("Rock, paper, scissors. Enter your choice here: ")
    # change user input to lower case
    user_choice = user_choice.lower()

    # computer choice
    computer_choice = random.randint(0, 2)

    # game logic
    # If the user types something that is not rock, paper, or scissors alert them of the error
    # loop until the user has entered a valid option
    while user_choice not in options:
        print("Your entry is not one of the three options. Try again: ")
        user_choice = input("Choose rock, paper, or scissors: ")

    # The random number 0-2 that the computer has selected will pull the corresponding option from the options list
    computer_choice = options[computer_choice]

    # same choice = draw
    if computer_choice == user_choice:
        print(computer_choice + " vs " + user_choice)
        print("Draw")
        print("Computer: " + str(computer_score) + "\tUser: " + str(user_score))
    # if computer = rock & user = paper: user wins
    elif computer_choice == options[0] and user_choice == options[1]:
        user_score = user_won(user_score)
    # if computer = rock & user = scissors: user loses
    elif computer_choice == options[0] and user_choice == options[2]:
        computer_score = computer_won(computer_score)
    # if computer = paper & user = rock: user loses
    elif computer_choice == options[1] and user_choice == options[0]:
        computer_score = computer_won(computer_score)
    # if computer = paper & user = scissors: user wins
    elif computer_choice == options[1] and user_choice == options[2]:
        user_score = user_won(user_score)
    # if computer = scissors & user = rock: user wins
    elif computer_choice == options[2] and user_choice == options[0]:
        user_score = user_won(user_score)
    # if computer = scissors & user = paper: user loses
    elif computer_choice == options[2] and user_choice == options[1]:
        computer_score = computer_won(computer_score)
    else:
        print("Something went wrong. An option was missed.")

    # the game will loop unless the user types stop
    continue_playing = input("'Stop' to end the game or 'Enter' to continue: ")
    print()
    if continue_playing.lower() == 'stop':
        break


