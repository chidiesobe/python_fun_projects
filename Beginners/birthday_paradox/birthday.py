import random
import datetime
from tabnanny import check

months = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
          7: 'Jul', 8: 'Aug', 9: 'Sept', 10: 'Oct', 11: 'Nov', 12: 'Dec'}

start_date = datetime.date(2022, 1, 1)
birthday = []
matching_birthday = []

# generate random birthday 
def generate_birthdays(birthdayNumber):
    for _ in range(birthdayNumber):
        random_day = random.randint(1, 365)
        current_date = start_date + datetime.timedelta(days = random_day)
        new_date = datetime.datetime.strptime(str(current_date), "%Y-%m-%d")
        birthday.append(str(new_date.day) + " " +months[new_date.month])
    return birthday

#enter the number of birthdays to be compared
enter_birthday = input('Enter the number of birthdays you want to compare, maximum to be 100: ')
check_birthday = generate_birthdays(int(enter_birthday))

# check if birthdays are unique
if len(check_birthday) == len(set(check_birthday)):
    print('All birthday are unique')
else:
    # check for matching birthdays 
    for keyA, valueA in enumerate(birthday):
        for keyB, valueB in enumerate(birthday[keyA + 1 :]):
            if valueA == valueB:
                matching_birthday.append(valueA)
    print('The following Birthdays Occured Multiple times')
    print(set(matching_birthday))