# Rock paper scissors game using random library
import random
while True:
    user = input('Enter "r" for rock, "p" for paper, or "s" for scissors: ')
    # asks user for input (rock, paper, or scissors)
    computer = random.choice(['r', 'p', 's'])
    # gets random choice from computer (rock, paper, or scissors)
    # all the situations for winning, losing, or tie-ing:
    if user == 'r' and computer == 's':
        print("Computer selected scissors and you won!")
    elif user == 'p' and computer == 'r':
        print('Computer selected Rock and you won!')
    elif user == 's' and computer == 'p':
        print('Computer selected Paper and you won!')
    elif user == 'r' and computer == 'r':
        print('Its a tie!')
    elif user == 'p' and computer == 'p':
        print('Its a tie!')
    elif user == 's' and computer == 's':
        print('Its a tie!')
    elif user == 'r' and computer == 'p':
        print('Computer selected paper and you lost!')
    elif user == 'p' and computer == 's':
        print('Computer selected scissors and you lost!')
    elif user == 's' and computer == 'r':
        print('Computer selected rock and you lost!')
    # asks user if they want to play again
    user2 = input('Do you want to play again?')
    if user2 == 'yes' or user2 == 'y':
        continue
    else:
        break
