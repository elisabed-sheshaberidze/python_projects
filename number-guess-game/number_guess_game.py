from random import randint
import string
import time

# constants
LOWEST_NUMBER = 1
MIN_POINT = -20
WINNING_POINT = 100
#  -- Define and validate user name --

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


def get_difficulty():
    return input('Please enter maximum number - 30, 50, 100 ')

def validate_difficulty():
    """This function validates the highest number from given range
     (rejects unwanted characters of numbers)
     and returns the highest number."""

    while True:
        highest_number = get_difficulty()
        if highest_number.strip() not in ['30', '50', '100']:
            print('Please enter valid number either 30, 50 or 100!')
            continue
        else:
            highest_number = int(highest_number)
            return highest_number


def generate_number(maximum):
    return randint(LOWEST_NUMBER, maximum)

def award_points(maximum_number):
    award = 0
    if maximum_number == 30:
        award = 5
    elif maximum_number == 50:
        award = 10
    elif maximum_number == 100:
        award = 20
    return award

def deduct_points(maximum_number):
    deduct = 0
    if maximum_number == 30:
        deduct = 2
    elif maximum_number == 50:
        deduct = 3
    elif maximum_number == 100:
        deduct = 8
    return deduct

# random number. tries=5. MIN_POINT = -20, WINNING_POINT = 100

def odd_or_even(number_to_guess):
    if number_to_guess % 2 == 0:
        return 'even'   
    else:
        return 'odd'    

def start_game(award, deduct, maximum_number):

    """This function starts the game. It generates a random number and asks user to guess it.
     It also counts points, the number of attempts and gives feedback to user."""
    
    total_points = 0
    while True:
        number_to_guess = generate_number(maximum_number)
        hint = odd_or_even(number_to_guess)
        want_to_quit = False
        total_tries = 5
        
        while True:
            try:
                guessed_number = input(f'Guess the number between {LOWEST_NUMBER} and {maximum_number}: Psst... The number is {hint}')

                
                if guessed_number.lower().strip() == 'quit':
                    want_to_quit = True
                    break
                if int(guessed_number) == number_to_guess:
                    total_points += award
                    print(f'Correct! You earned {award} points! Your total points: {total_points}')
                    break
                elif int(guessed_number) < number_to_guess:
                    print(f'Too low! You lost {deduct} points! Your total points: {total_points}')
                    total_tries -= 1
                    total_points -= deduct
                elif int(guessed_number) > number_to_guess:
                    print(f'Too high! You lost {deduct} points! Your total points: {total_points}')
                    total_tries -= 1
                    total_points -= deduct
                if total_tries == 0:
                    print(f'No more tries left! The correct number was - "{number_to_guess}".')
                    print(f'your total points: {total_points}')
                    break 

            except ValueError:
                print('Please enter a valid number!')
                continue

        if want_to_quit:
            break

        if total_points <= MIN_POINT:
            print('You lost the game! 😞')
            break
        elif total_points >= WINNING_POINT:
            print('Congratulations! You won the game! 🥳' \
            'You are the master of numbers! 🧙️')
            break
    



# program runs here
def rules(user):
    """Rules of games. This function explains what players can do."""

    print(f'''Welcome {user} to the Number Guessing Game!
                          Here are rules😁
          • First, you must choose the game difficulty level.
          • 30 - easy mode; 50 - medium; 100 - hard mode.
          • Then, you will have to guess the number that the game will generate.
          • You will get points for each correct guess and lose points for each wrong guess.
          • The points you get or lose depend on the difficulty level you choose.
          • Rewards: easy mode +5 points, medium mode +10 points, hard mode +20 points.
          • Penalties: easy mode -2 points, medium mode -3 points, hard mode -8 points.

          note: Type quit to exit the game at any time.
        =======================================================================================
                                        GOOD LUCK! 🍀

    ''')


def main():
    user = validate_username()
    maximum_number = validate_difficulty()
    award = award_points(maximum_number)
    deduct = deduct_points(maximum_number)

    rules(user)
    start_game(award, deduct, maximum_number)


if __name__ == '__main__':
    main()



