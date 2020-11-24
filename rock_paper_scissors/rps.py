
import os
import random
rock = '''
    ____
---'____)
    (_____)
    (_____)
    (____)
---._(___)
'''

paper = '''
    ________
---'    ____)
        ______)
        _______)
        _______)
---.__________)
'''

scissors = '''
    ______
---'  ____)___
        ______)
    __________)
    (____)
---._(___)
'''

"""
RULES:
0 Rock wins against scissors. --- 0/2
1 Paper wins against rock. --- 1/0
2 Scissors win against paper. --- 2/1
"""


guess = [rock, paper, scissors]
os.system('clear')
print('0: for ROCK, 1: for PAPER, 2: for SCISSORS \n')
user_guess = input('Kindly make a choice: ')

if user_guess.isdigit() and int(user_guess) < 3:
    user_guess = int(user_guess)
    while True:
        computer_guess = random.randint(0, len(guess) - 1)
        if user_guess == computer_guess:
            print(f'You both selected {guess[user_guess]}')
            response = input(
                'You have a draw, do you want to play again ... Y for YES , N for NO: ')
            if response.lower() == 'y':
                os.system('clear')
                print('0: for ROCK, 1: for PAPER, 2: for SCISSORS \n')
                user_guess = input('Kindly make a choice: ')
                if user_guess.isdigit() and int(user_guess) < 3:
                    user_guess = int(user_guess)
                    continue
                else:
                    print('hate to see you go, GOODBYE!!!')
                    break
        elif user_guess == 0 and computer_guess == 2:
            print('YOU WIN!!!!')
            print(f'YOU: {guess[user_guess]}')
            print(f'COMPUTER: {guess[computer_guess]}')
            break
        elif user_guess == 2 and computer_guess == 0:
            print('YOU LOSE!!!!')
            print(f'YOU: {guess[user_guess]}')
            print(f'COMPUTER: {guess[computer_guess]}')
            break
        elif user_guess > computer_guess:
            print('YOU WIN!!!!')€
            print(f'YOU: {guess[user_guess]}')
            print(f'COMPUTER: {guess[computer_guess]}')
            break
        else:
            print('YOU LOSE!!!!')
            print(f'YOU: {guess[user_guess]}')
            print(f'COMPUTER: {guess[computer_guess]}')
            break
else:
    print('invalid number, GAME OVER')


# YOUTUBE VIDEO EXPLAINING THIS SCRIPT
# https://www.youtube.com/watch?v=KOvsLhv2EhE&t=150s