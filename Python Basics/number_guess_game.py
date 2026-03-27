# # goal: create simple game where the player has to guess game and gather points
# # rules: player chooses scope 1-15, 1-30, 1-50
# # has to collect 100 points
# # has 5 attempts. correct answer +5, +10, +20 points ( 1-15, 1-30, 1-50). If wrong - same score
# # will have hints. Odd/even always
# # rules
import random
import turtle
import time
# player name
def get_username():
    print('Hello, player!')
    time.sleep(1.5)
    while True:
        player = input(
            'Please enter your name! (Only letters/digits and no space): ')
        cln_player = player.strip()
        if cln_player.isalnum():
            return cln_player
        else:
            print('Oops, please use only letters and digits wiith no space.')
def rules():
    print(f'''Welcome {player_name} to the Number Guessing Game!
            Here is you guide:
          1) First you must difficulty level (easy: 1-10, medium: 1-30 or hard: 1-50).
          2) Your goal is to collect 100 scores.
          3) You have 5 tries to guess the number
          4) If you fail you lose points, if you win, you gain
          Point system:
           - + or - 5 points if the scope is 1-10
           - + or - 10 points if the scope is 1-30
           - + or - 20 points if the scope is 1-50
    ''')
# game difficulty
def game_difficulty():
    print('Please choose the difficulty level of the game ')
    while True:
        try:
            difficulty = int(input('easy: 15, medium: 30 or hard: 50. '))
            if difficulty in [15, 30, 50]:
                return difficulty
            else:
                print('Reminder: limit must be either 15, 30, or 50: ')
        except ValueError:
            print('Please enter the number!')
difficulty_level = game_difficulty()
def score_system():
    if difficulty_level == 15:
        score = 5
    elif difficulty_level == 30:
        score = 10
    else:
        score = 20
    return score
def winners_surprise():
    print('Congratulations! You win!')
    time.sleep(2)
    print('I have a surprise :)')
    time.sleep(2)
    print('Ready...')
    time.sleep(2)
    t = turtle.Turtle()
    s = turtle.Screen()
    s.title('Click to exit!')
    s.bgcolor('#f8edeb')
    t.write("\"The most certain way to succeed is always to try just one more time.\" — "
            "Thomas Edison", align="center", font=("Verdana", 10, "normal"))
    turtle.exitonclick()
def play_game():
    total_score = 0
    while total_score < 100:
        number_to_guess = random.randint(1, difficulty_level)
        tries = 5
        while tries > 0:
            try:
                if number_to_guess % 2 == 0:
                    print('The number is even')
                else:
                    print('The number is odd')
                guessed_number = int(input('Take a guess! '))
                if guessed_number == number_to_guess:
                    print('Good job! You guessed the number! Here is you point')
                    total_score += score_system()
                    print(f'Your total score is {total_score}')
                    break
                else:
                    print('Oops, not your lucky try! Guess again!')
                    tries -= 1
                if tries == 0:
                    total_score -= score_system()
                    print(f'The number was {number_to_guess}! Here is your current score: {total_score}')
            except ValueError:
                print('Hmm... ypu have to guess number. Please enter a number!')
        if total_score == 100:
            winners_surprise()
player_name = get_username()
rules()
play_game()
