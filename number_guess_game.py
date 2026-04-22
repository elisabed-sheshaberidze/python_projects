# in this "Number Guessing Game" player can choose a range and keep track of their progress.
from random import randint
import string
import time

# constants
LOWEST_NUMBER = 1



#  -- I define and validate user name --

def get_username():
    return input('Please enter a username! ')

def validate_username():
    """This function cleans the user name. rejects if it contains invalid characters - anything other
    that letters, digits and underscores """
    print('Username can contain only letters, numbers and underscores.')

    allowed = string.ascii_letters + string.digits + '_'
    while True:
        raw_username = get_username()
        cln_username = raw_username.strip().lower()
        if not cln_username:
            print('Please enter a username!')
            continue
        elif len(cln_username) < 4 or len(cln_username) > 20:
            print('Username is too short/long!')
            continue
        elif not all(char in allowed for char in cln_username):
            print('Username contains invalid characters!')
            continue
        else:
            return cln_username



# User chooses game difficulty based on the number range
# 30 - easy mode; 50 - medium; 100 - hard mode.


def get_highest_number():
    return input('Please enter max number - 30, 50, 100 ')

def validate_highest_number():
    """This function validates the highest number from given range
     (rejects unwanted characters of numbers)
     and returns the highest number."""

    while True:
        highest_number = get_highest_number()
        if highest_number.strip() not in ['30', '50', '100']:
            print('Please enter valid number either 30, 50 or 100!')
            continue
        else:
            highest_number = int(highest_number)
            return highest_number

def number_range(maximum=30):
    return randint(LOWEST_NUMBER, maximum)






def rules():
    """Rules of games. This function explains what players can do."""

    print(f'''Welcome {user} to the Number Guessing Game!
          {time.sleep(2)}
          Here are rules😁
          • First, you must choose the game difficulty level.
          •
    ''')
user = validate_username()
max_number = validate_highest_number()

def main():
    pass

if __name__ == '__main__':
    main()


