import sqlite3

CREATE_PRODUCTS_TABLE = 'CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, description TEXT , price FLOAT , quantity INTEGER);'

ADD_PRODUCT = 'INSERT INTO products (name, description, price, quantity) VALUES (?, ?, ?, ?);'

GET_ALL_PRODUCTS = 'SELECT * FROM products'

SEARCH_PRODUCT_BY_NAME = 'SELECT * FROM products WHERE name = ?'

REMOVE_PRODUCT = 'DELETE FROM products WHERE name = ?'

GET_BEST_PRODUCT = 'SELECT * FROM products ORDER BY rating DESC LIMIT 1'

UPDATE_PRODUCT = 'UPDATE products SET name = ?, description = ?, price = ?, quantity = ? WHERE id = ?'

 #|<--------------products queries---------------->|
 
# CREATE_HISTORY_TABLE = 'CREATE TABLE IF NOT EXISTS history (id INTEGER PRIMARY KEY, product_id INTEGER, quantity INTEGER, total FLOAT, date TEXT);'

CREATE_USERS_TABLE = 'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,First_Name TEXT , Last_Name TEXT , Email TEXT, Username TEXT, Password TEXT , Phone_number INTEGER);'

GET_ALL_USERS = 'SELECT * FROM users'

SEARCH_USER = 'SELECT * FROM users WHERE Username = ?' #for admin

SEARCH_EMAIL = 'SELECT COUNT(*) FROM users WHERE Email = ?'

ADD_USER = 'INSERT INTO users (First_Name, Last_Name, Email, Username, Password, Phone_number) VALUES (?, ?, ?, ?, ?, ?);'

USER_LOGIN = 'SELECT COUNT(*) FROM users WHERE Username = ? AND Password = ?'

USERNAME_VALIDATION = 'SELECT COUNT(*) FROM users WHERE Username = ?'

GET_USER_DETAILS = 'SELECT * FROM users WHERE Username = ?'

UPDATE_USER_PASSWORD = 'UPDATE users SET Password = ?, WHERE Username = ?'

UPDATE_USER_EMAIL = 'UPDATE users SET Email = ?, WHERE Username = ?'

GET_USER_BY_ID = 'SELECT * FROM users WHERE id = ?'

#<------------------ADMIN queries------------------->|

CREATE_ADMINS_TABLE = 'CREATE TABLE IF NOT EXISTS admins (id INTEGER PRIMARY KEY, username TEXT, password TEXT);'

ADD_ADMIN = 'INSERT INTO admins (username, password) VALUES (?, ?);'

GET_ALL_ADMINS = 'SELECT * FROM admins'

ADMIN_LOGIN = 'SELECT password FROM admins WHERE username = ?'

REMOVE_USER = 'DELETE FROM users WHERE id = ?'

SEARCH_ADMIN = 'SELECT * FROM admins WHERE username = ?'

REMOVE_ADMIN = 'DELETE FROM admins WHERE id = ?'

CHECK_ADMIN_USERNAME = 'SELECT COUNT(*) FROM admins WHERE username = ?'

#<------------------USER HISTORY queries------------------->|

WRITE_HISTORY = 'INSERT INTO history (username, product_id, product_name, quantity, total, date) VALUES (?, ?, ?, ?, ?, ?);'

CREATE_USERS_HISTORY_TABLE = 'CREATE TABLE IF NOT EXISTS history (history_id INTEGER PRIMARY KEY, username TEXT, product_id TEXT, product_name TEXT, quantity TEXT, total FLOAT, date TEXT);'

GET_HISTORY = 'SELECT * FROM history WHERE username = ?'

def connect():
    return sqlite3.connect('data.db')

def create_product_tables(connection):
    with connection:
        connection.execute(CREATE_PRODUCTS_TABLE)
        
def add_product(connection, name, description, price, quantity):
    with connection:
        connection.execute(ADD_PRODUCT, (name, description, price, quantity))
        
def get_all_products(connection):
    with connection:
        return connection.execute(GET_ALL_PRODUCTS).fetchall()
    
def search_product_by_name(connection, name):
    with connection:
        result = connection.execute(SEARCH_PRODUCT_BY_NAME, (name,)).fetchall()
    if not result:
        return "No product found with that name"
    else:
        return result
    
def remove_product(connection, name):
    with connection:
        connection.execute(REMOVE_PRODUCT, (name,))

def update_product_in_db(connection, product_id, name, description, price, quantity):
    """
    Updates a product in the database with the provided details.
    """
    try:
        # Execute the update query
        connection.execute(UPDATE_PRODUCT, (name, description, price, quantity, product_id))
        # Commit the changes
        connection.commit()
    except Exception as e:
        # rollback the transaction if needed
        connection.rollback()

#<------------------users queries------------------->|

def add_user(connection, First_Name, Last_Name, E_mail, Username, Password, Phone_number):
    with connection:
        connection.execute(ADD_USER, (First_Name, Last_Name, E_mail, Username, Password, Phone_number))
        
def create_users_table(connection):
    with connection:
        connection.execute(CREATE_USERS_TABLE)
        
def check_email(connection, E_mail):
    with connection:
        result = connection.execute(SEARCH_EMAIL, (E_mail,)).fetchone()
        if result and result[0] > 0:
            return True # Email is taken
        else:
            return False # Email is available
        
def username_validation(connection, Username):
    with connection:
        result = connection.execute(USERNAME_VALIDATION, (Username,)).fetchone()
        if result and result[0] > 0: 
            return True  # Username is taken
        else:
            return False  # Username is available
        
def login_validation(connection, Username, Password):
    with connection:
        result = connection.execute(USER_LOGIN,(Username, Password)).fetchone()
        
        return result and result[0] > 0
        
def get_user_details(connection, Username):
    with connection:
        return connection.execute(GET_USER_DETAILS, (Username,)).fetchall()[0]
    
def update_user_password(connection, Password, Username):
    with connection:
        connection.execute(UPDATE_USER_PASSWORD, (Password, Username))
        
def update_user_email(connection, Email, Username):
    with connection:
        connection.execute(UPDATE_USER_EMAIL, (Email, Username))
        
def list_users(connection):
    with connection:
        return connection.execute(GET_ALL_USERS).fetchall()
    
def search_user(connection, Username):
    with connection:
        return connection.execute(SEARCH_USER, (Username,)).fetchall()[0]
    
def get_user_by_ID(connection, user_id):
    try:
        with connection:
            return connection.execute(GET_USER_BY_ID, (user_id,)).fetchall()[0]
    except Exception as e:
        print('\nUser not found')

    
#<------------------ADMIN queries------------------->|

def create_admins_table(connection):
    with connection:
        connection.execute(CREATE_ADMINS_TABLE)
        
def add_admin(connection, username, password):
    with connection:
        connection.execute(ADD_ADMIN, (username, password))
        
def list_admins(connection):
    with connection:
        return connection.execute(GET_ALL_ADMINS).fetchall()
    
def admin_login(connection, username, password):
    with connection:
        result = connection.execute(ADMIN_LOGIN, (username, password)).fetchall()
        if result:
            return True
        else:
            return False
        
def remove_user(connection, user_id):
    with connection:
        connection.execute(REMOVE_USER, (user_id,))
        
def admin_username_validation(connection, username):
    with connection:
        result = connection.execute(SEARCH_ADMIN, (username,)).fetchall()
        if result:
            return False
        else:
            return True

def remove_admin(connection, id):
    with connection:
        connection.execute(REMOVE_ADMIN, (id,))

#<------------------USER HISTORY queries------------------->|

def create_users_history_table(connection):
    with connection:
        connection.execute(CREATE_USERS_HISTORY_TABLE)
        
def write_history(connection, username, product_id, product_name, quantity, total, date):
    with connection:
        connection.execute(WRITE_HISTORY, (username, product_id, product_name, quantity, total, date))
        
def get_history(connection, username):
    with connection:
        return connection.execute(GET_HISTORY, (username,)).fetchall()