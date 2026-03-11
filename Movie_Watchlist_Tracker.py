# Goal:
# to track movies user wants to watch, then already watched movies
import string
def get_username():
    """this function will return a username"""
    while True:
        user = input("Enter your username: ").strip()
        if not user:
            print('Your name must contain characters (letters, numbers)')
        elif len(user) < 3:
            print('Your name must be at least 3 characters long')
        elif len(user) > 20:
            print('Your name must be at most 20 characters long')
        elif any(char in string.punctuation for char in user):
            print('Your name must not contain punctuation')
        else:
            return user
want_to_watch = []
def add_movie():
    """this function will add a movie to your wishlist"""

    print('if you would like to exit wishlist, enter "quit"')
    while True:
        movie_name = input("Enter the movie name you would like to add watch wishlist: ")
        movie_name = string.capwords(movie_name).strip()
        if movie_name == 'Quit':
            break
        elif movie_name not in want_to_watch:
            want_to_watch.append(movie_name)
        else:
            print(f'This movie is already in your wishlist!')
        print(want_to_watch)
# user removes film
def remove_movie():
    """this function will remove a movie from your wishlist"""

    print('if you would like to exit, enter "quit"')
    while True:
        rmv_movie_name = input("Enter the movie name you would like to remove watch wishlist: ")
        rmv_movie_name = string.capwords(rmv_movie_name).strip()
        if rmv_movie_name == 'Quit':
            break
        elif rmv_movie_name  in want_to_watch:
            want_to_watch.remove(rmv_movie_name)
        else:
            print(f'This movie is not in your wishlist!')
def what_user_wants():
    """this function will ask user what they want to do;
    see wishlist, add movie or remove movie from your wishlist
    """
    print('What would you like to do?')
    while True:
        print('''
        1 - seeing watchlist
        2 - add movie
        3 - remove movie
        ''')
        action = input('Please enter your choice number: ').strip()
        if not action:
            print('please enter your choice number')
        elif action not in ['1', '2', '3']:
            print('please enter your choice number 1, 2, or 3')
        elif action == '1':
            print(f'here is your wishlist: {want_to_watch}')
        elif action == '2':
            add_movie()
        elif action == '3':
            remove_movie()
username = get_username()
print(f'Welcome {username}!')
what_user_wants()