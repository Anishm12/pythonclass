# Game to guess the number
import random
num = random.randint(1, 9)
guess = False
counter = 0
while not guess:
    usernum = int(input('Enter a number between 0 and 9: '))
    if usernum == num:
        guess = True
    elif usernum < num:
        print('Too low!')
        counter = counter + 1
        print(f'You guessed it wrong. You have {3 - counter} more tries')

    else:
        print('Too high!')
        counter = counter + 1
        print(f'You guessed it wrong. You have {3 - counter} more tries')
        if counter == 3:
            print()
if guess:
    print('You guessed it right!')
else:
    print('You lost!')
    print(f'The number was {num}!')
