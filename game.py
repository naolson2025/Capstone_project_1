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

# global list and score. 
options = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

def main():
    print("Beat the program!")
    while True:
        user_decision = user_input()
        computer_decision = computer_input()
        game_logic(computer_decision, user_decision)

        # the game will loop unless the user types stop
        continue_playing = input("'Stop' to end the game or 'Enter' to continue: ")
        print()
        if continue_playing.lower() == 'stop':
            break


def user_input():
    # Input from user
    user_choice = input("Rock, paper, scissors. Enter your choice here: ").lower()
    # If the user types something that is not rock, paper, or scissors alert them of the error
    # loop until the user has entered a valid option
    while user_choice not in options:
        print("Your entry is not one of the three options. Try again: ")
        user_choice = input("Choose rock, paper, or scissors: ")
    return user_choice

def computer_input():
    # computer choice, get a random # 0-2 then find the corresponding option in the options list
    computer_choice = random.randint(0, 2)
    return options[computer_choice]

# call if there is a draw
def draw(computerDecision, userDecision):
    formatter(computerDecision, userDecision, 'Draw')

# call this method if the computer won the match
# print in table
def computer_won(computer_decision, user_decision):
    # Found global on stackoverflow
    global computer_score
    computer_score += 1
    formatter(computer_decision, user_decision, 'You lost')

# call this method if the user won the match
# print in a table
def user_won(computer_decision, user_decision):
    global user_score
    user_score += 1
    formatter(computer_decision, user_decision, 'You won!')

# formats results into a table
def formatter(computerChoice, userChoice, result):
    print()
    # found center align on pyformat.info
    print('{:^30}'.format('Results'))
    print()
    #print(computer_choice + " vs " + user_choice)
    print('{:5} {:13} {:10}'.format('', 'Computer', 'You'))
    print('{:5} {:13} {:10}'.format('', computerChoice, userChoice))
    print()
    print('{:^30}'.format(result))
    print()
    print("Computer: " + str(computer_score) + "\tUser: " + str(user_score))
    print()

def game_logic(computerDecision, userDecision):
    # same choice = draw
    if computerDecision == userDecision:
        draw(computerDecision, userDecision)
    # if computer = rock & user = paper: user wins
    elif computerDecision == options[0] and userDecision == options[1]:
        user_won(computerDecision, userDecision)
    # if computer = rock & user = scissors: user loses
    elif computerDecision == options[0] and userDecision == options[2]:
        computer_won(computerDecision, userDecision)
    # if computer = paper & user = rock: user loses
    elif computerDecision == options[1] and userDecision == options[0]:
        computer_won(computerDecision, userDecision)
    # if computer = paper & user = scissors: user wins
    elif computerDecision == options[1] and userDecision == options[2]:
        user_won(computerDecision, userDecision)
    # if computer = scissors & user = rock: user wins
    elif computerDecision == options[2] and userDecision == options[0]:
        user_won(computerDecision, userDecision)
    # if computer = scissors & user = paper: user loses
    elif computerDecision == options[2] and userDecision == options[1]:
        computer_won(computerDecision, userDecision)
    else:
        print("Something went wrong. An option was missed.")

main()