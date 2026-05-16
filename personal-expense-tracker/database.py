import sqlite3

def connect_db():
    """Connects to the SQLite database and returns cursor object for executing SQL commands."""
    conn = sqlite3.connect('expense_tracker.db')
    return conn

def create_user_table():
    '''Creates the users table in the database if it doesn't already exist.'''
    with connect_db() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL)
''')

def insert_information(username, password):
    '''Inseets a new user into the users table.'''
    with connect_db() as conn:
        conn.execute('''INSERT INTO users (username, password)
                     VALUES(?, ?)''', (username, password))

def delete_user(username):
    '''Deletes a user from the user table based on the provided username.'''
    with connect_db() as conn:
        conn.execute('''DELETE FROM users WHERE username = ?''', (username,))

