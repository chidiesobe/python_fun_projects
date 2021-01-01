import random 

# number of trials left till game over and the guesses made by the user
trials = 0 
guess = 0

# accepts user input greater than 2
num_limit = input('Please enter a number greater than 2 as the guess limit: ')

# verify the value of the num_limit is a digit
if(num_limit.isdigit()):
    # generate the random number to be guessed by the user, using the random() function
    rand  = random.randint(1, int(num_limit))
    # user is allow to make three trials at guessing the random number
    while trials < 3: 
        if num_limit.isdigit() and int(num_limit) > 2: 
            print(f'You have chosen to guess a random number between 1 and {num_limit}')
            print(f'You have {3 - trials} guess(es) left')

            guess = input('Kindly make your guess: ')
            if guess.isdigit() and guess != rand:
                trials += 1 #increase the trial values by 1
            else: 
                guess = input('Kindly make a numerical guess: ')
                trials += 1 
                continue # while loops keeps running
        else: 
            print('You have entered an invalid number, please try again: ')
            num_limit = input('Please enter a number greater than 2 as the guess limit: ')
        if int(guess) == rand: 
            print(f'CONGRATULATION, YOUR GUESS OF {guess} IS CORRECT')
            break #stops the while loop
    if trials > 2 and int(guess) != rand:
        print(f'GAME OVER, YOU HAVE FAILED TO GUESS THE RIGHT NUMBER !!! THE RIGHT NUMBER WAS {rand}')
else:
    print('You entered and invalid number')


# YOUTUBE VIDEO EXPLAINING THIS SCRIPT
# https://www.youtube.com/watch?v=fYdrdJVabm0