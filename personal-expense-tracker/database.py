import sqlite3

def connect_db():
    """Connects to the SQLite database and returns the connection object."""
    return sqlite3.connect('expense_tracker.db')

def cursor():
    """Returns cursor object for executing SQL commands."""
    return connect_db().cursor()

def create_user_table():
    with connect_db() as conn:
        cursor().execute('''
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username )
''')
