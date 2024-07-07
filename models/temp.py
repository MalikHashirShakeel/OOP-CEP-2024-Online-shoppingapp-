import database
import bcrypt


connection = database.connect()
connection.isolation_level = None

import bcrypt
import sqlite3

# SQL Query for Admin Login

def add_admin():
    while True:
        print("\n==============================")
        print("     Add Admin User")
        print("==============================\n")
        username = input("Enter admin username: ").lower().strip()
        
        # Check if the username already exists
        if username_exists(connection, username):
            print("\n⚠️  Username is already taken! Please choose another username.\n")
            continue
        
        password = input("Enter admin password: ").strip()
        confirm_password = input("Confirm password: ").strip()

        if password != confirm_password:
            print("\n⚠️  Passwords do not match! Please try again.\n")
            continue
        
        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        try:
            # Insert the new admin user into the database
            with connection:
                connection.execute(database.ADD_ADMIN, (username, hashed_password))
            print("\n✅  Admin user added successfully.\n")
            break
        except sqlite3.IntegrityError as e:
            print(f"\n❌  Error adding admin user: {e}\n")
            continue
    

def username_exists(connection, username):
    with connection:
        result = connection.execute(database.CHECK_ADMIN_USERNAME, (username,)).fetchone()
        return result and result[0] > 0  # Returns True if username exists

def admin_login():
    while True:
        print("\n==============================")
        print("        Admin Login")
        print("==============================\n")
        username = input("Admin Username: ").lower().strip()
        password = input("Admin Password: ").strip()  

        if validate_admin_credentials(connection, username, password):
            print(f"\n✅  Login successful. Welcome, {username}!\n")
            connection.close()
            return username  
        else:
            print("\n❌  Login failed. Invalid username or password. Please try again.\n")
    


def validate_admin_credentials(connection, username, password):
    with connection:
        result = connection.execute(database.ADMIN_LOGIN, (username,)).fetchone()
        if result:
            stored_hashed_password = result[0]
            # Validate the password using bcrypt
            if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password):
                return True
        return False

            
if __name__ == '__main__':
    if (choice := input('Do you want to create an admin? (y/n): ')) == 'y' or choice == 'Y':
        add_admin()
    else:
        admin_login()