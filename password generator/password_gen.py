import random
import string
import math

special_character = ['#', '$', '%', '&', '@', '?', '_', '.', '(', ')']
special_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

alphabetUpper = string.ascii_uppercase
alphabetLower = string.ascii_lowercase
password = []

password_length = int(input('Enter the password lenght \n'))

if password_length > 5:
    average = math.floor(password_length / 2)
    numbers = password_length - average

    for _ in range(numbers):
        password += random.choice(special_numbers)
    for _ in range(average):
        password += random.choice(special_character)
    if password_length % 2 == 0:
        alphabet_select = 2
    else:
        alphabet_select = 3
    for _ in range(alphabet_select):
        password[random.randint(0, password_length - 1)] = random.choice(alphabetUpper)
        password[random.randint(0, password_length - 1)] = random.choice(alphabetLower)
    print(password)
    new_password = ''.join(map(str, random.sample(password, password_length)))
    print(new_password)

else:
    print('Password length must be greater than 5')
