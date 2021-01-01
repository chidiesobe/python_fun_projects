import random 
import os 
from hangman_words import possible_words
from hangman_ascii import HANGMANPICS

# code that won't repeat themselve

selected_words = random.choice(possible_words)
guess = []
trials = 0
for word_count in range(len(selected_words)):
    guess.append(' _ ')

#end of codes that won't repeat themselves

while trials < 7:
    print(f'YOU HAVE {7- trials} TRIAL(S) LEFT \n')
    print(f'{guess} \n')
    user_guess = input('Guess a matching letter in the word aboe \n').lower()
    os.system('clear')
    for i in range(len(selected_words)):
        verify = selected_words[i]
        if user_guess == selected_words[i]:
            guess[i] = user_guess
        elif user_guess not in selected_words:
            print(HANGMANPICS[trials])
            trials += 1
            break

    # check to see all correct guessed 
    if ' _ ' not in guess: 
        print('CONGRATULATIONS YOU HAVE WON THE GAME \n')
        print(f'THE WORD WAS {selected_words.upper()}')
        print(f'{guess} \n')
        break

if trials == 7:
    print('YOU LOST THE GAME')
    print(f'THE WORD WAS {selected_words.upper()}')