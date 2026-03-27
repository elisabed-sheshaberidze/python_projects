# Goal:
# to track movies user wants to watch, then already watched movies
from string import punctuation, capwords

# we define user name
def get_username():
    """this function will return a username"""
    while True:
        user = input("Enter your username: ").strip()
        if not user:
            print('Your name must contain characters (letters, numbers)')
        elif len(user) < 3 or len(user) > 20:
            print('Your name must be between 3 and 20 characters')
        elif any(char in punctuation for char in user):
            print('Your name must not contain punctuation')
        else:
            return user
# user name

def add_movie(wish_list):
    """this function will add a movie to your wishlist"""
    print('if you would like to exit wishlist, enter "quit"')
    while True:
        movie_name = input("Enter the movie name you would like to add watch wishlist: ")
        movie_name = capwords(movie_name).strip()
        if movie_name == 'Quit':
            break
        elif movie_name not in wish_list:
            wish_list.append(movie_name)
            print(f'Movies in your Wish List: {wish_list}')

        else:
            print(f'This movie is already in your wishlist!')
        print(wish_list)

# user removes film
def remove_movie(wish_list, user_name):
    """this function will remove a movie from your wishlist"""

    print(f'{user_name}, if you would like to exit, enter "quit"')
    while True:
        rmv_movie_name = input("Enter the movie name you would like to remove watch wishlist: ")
        rmv_movie_name = capwords(rmv_movie_name).strip()
        if rmv_movie_name == 'Quit':
            break
        elif rmv_movie_name  in wish_list:
            wish_list.remove(rmv_movie_name)
            print(f'Movies in your Wish List: {wish_list}')
        else:
            print(f'This movie is not in your wishlist!')

# what user wants
def what_user_wants(wish_list, user_name):
    """this function will ask user what they want to do;
    see wishlist, add movie or remove movie from your wishlist
    """
    print('What would you like to do?')
    print('''
            1 - seeing watchlist
            2 - add movie
            3 - remove movie
            4 - if you want to quit
            ''')
    while True:
        action = input('Please enter your choice number: ').strip()
        if action not in ['1', '2', '3', '4']:
            print('please enter your choice number 1, 2, 3 or 4')
        elif action == '1':
            print(f'Here is your wishlist: {wish_list}')
        elif action == '2':
            add_movie(wish_list)
        elif action == '3':
            remove_movie(wish_list)
        elif action == '4':
            print(f'{user_name}, here is your current wishlist: {wish_list}')
            break

def main():
    user_name = get_username()
    wish_list = []
    what_user_wants(wish_list, user_name)

main()