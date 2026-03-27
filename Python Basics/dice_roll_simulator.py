from random import randint
def get_dice():
    dice = randint(1, 6)
    return dice
print(f'The number on the dice is:  {get_dice()}')
