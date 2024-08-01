from .User_class import User  # Import User class from User_class module
from .Admin_class import Admin #Import Admin class from Admin_class module
import random
import string
import re
import os
import time
from .db_functions import add_user,get_user_details,admin_login,list_all_users,get_user_by_ID,remove_user,list_admins,add_admin,remove_admin,list_all_products,remove_product,add_product,update_product
from . import database
from getpass import getpass


class System:

    def __init__(self):
        self.active_user = None
        connection = database.connect()
        connection.isolation_level = None
        database.create_users_table(connection)
        database.create_admins_table(connection)

#------------------------------------------CLEAR SCREEN------------------------------------------------------------------------------------

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

#------------------------------------------DISPLAY MENU------------------------------------------------------------------------------------

    def display_menu(self):
        self.clear_screen()
        print("\n")
        print("===============================================")
        print("|                                             |")
        print("|        Welcome to PRISTINE PICKS            |")
        print("|                  .v2                        |")
        print("===============================================")
        print("|                                             |")
        print("|  1. Signup                                  |")
        print("|  2. Login                                   |")
        print("|  3. Login as admin                          |")
        print("|  4. Exit                                    |")
        print("|                                             |")
        print("===============================================")
        print("\n")
        self.active_user = None


#--------------------------------------------RUN INTERFACE----------------------------------------------------------------------------------

    def run(self):
        connection = database.connect()
        connection.isolation_level = None
        
        while True:
            self.display_menu()
            choice = input("\nEnter your choice: ")

            if choice == '1':
                
                self.signup()
            
            elif choice == '2':
               
               self.active_user = None 
               if self.login():
                    return System.user_interface(self.active_user.get_username(),self.active_user)
                # return 'User'
            
            elif choice == '3':
                
                self.active_user = None
                self.admin_login()
                print("\nLogged in as Admin succcessfully!")
                self.admin_interface()
                # return 'Admin'
            
            elif choice == '4':
                print("\nExiting the application.")
                self.active_user = None
                break
            else:
                print("\nInvalid choice. Please try again.")


#------------------------------------------------CHECK FOR FIRST AND LAST NAMES------------------------------------------------------------

    @staticmethod
    def valid_first_name():
         while True:
                print("\n==============================")
                print("        First Name Entry")
                print("==============================\n")
                name = input("Enter your name here: ").upper().strip()

                if not name:
                    print("\n⚠️  You cannot leave the name empty. Please try again.\n")
                elif any(char.isdigit() for char in name):
                    print("\n⚠️  Your name cannot contain numbers. Please try again.\n")
                elif any(char in "!@#$%^&*()_-+=" for char in name):
                    print("\n⚠️  Your name cannot contain special characters. Please try again.\n")
                elif " " in name:
                    print("\n⚠️  Your name cannot contain blank spaces. Please try again.\n")
                else:
                    print("\n✅  Name successfully validated.\n")
                    return name
                
    @staticmethod
    def valid_last_name():
         while True:
                print("\n==============================")
                print("        Last Name Entry")
                print("==============================\n")
                l_name = input("Enter your name here: ").upper().strip()

                if not l_name:
                    print("\n⚠️  You cannot leave the name empty. Please try again.\n")
                elif any(char.isdigit() for char in l_name):
                    print("\n⚠️  Your name cannot contain numbers. Please try again.\n")
                elif any(char in "!@#$%^&*()_-+=" for char in l_name):
                    print("\n⚠️  Your name cannot contain special characters. Please try again.\n")
                elif " " in l_name:
                    print("\n⚠️  Your name cannot contain blank spaces. Please try again.\n")
                else:
                    print("\n✅  Name successfully validated.\n")
                    return l_name


#-------------------------------------------------CHECK FOR USERNAME------------------------------------------------------------

    def valid_username(self):
        connection = database.connect()
        connection.isolation_level = None

        while True:
            print("\n==============================")
            print("         Username Entry         ")
            print("==============================\n")
            username = input(
                "(Note: The username must be between 5 and 15 characters long,\n"
                "and can only contain letters and numbers.)\n"
                "\nEnter Username: "
            ).lower().strip()

            # First, check if the username is empty
            if not username:
                print("\n⚠️  You cannot leave the username portion empty. Please try again.\n")
                continue

            # Check if the username length is within the required range
            if len(username) < 5 or len(username) > 15:
                print("\n⚠️  Please use a username within the given range (5 to 15 characters). Please try again.\n")
                continue

            # Check for blank spaces
            if " " in username:
                print("\n⚠️  You cannot add blank spaces in your username. Please try again.\n")
                continue

            # Check for special characters
            if not username.isalnum():
                print("\n⚠️  Your username can only contain letters and numbers. Please try again.\n")
                continue

            # Check if username contains both letters and numbers
            if username.isalpha() or username.isdigit():
                print("\n⚠️  Your username must contain both letters and numbers. Please try again.\n")
                continue

            # Check if the username is already taken
            if database.username_validation(connection, username):
                print("\n⚠️  Username is already taken! Please try again.\n")
                continue

            # If all checks pass, the username is valid and not taken
            print("\n✅  Username successfully validated.\n")
            connection.close()
            return username



#-----------------------------------------------------GENERATE RANDOM PASSWORD------------------------------------------------------------
 
    @staticmethod
    def generate_random_password():
        length = random.randint(8, 15)

        # Ensure the password contains at least one letter, one number, and one special character
        letters = random.choices(string.ascii_letters, k=length - 3)
        digits = random.choices(string.digits, k=1)
        special_chars = random.choices("!@#$%^&*()-_+=", k=1)

        # Combine all characters
        all_chars = letters + digits + special_chars
        random.shuffle(all_chars)

        # Ensure the final length matches the required length
        while len(all_chars) < length:
            all_chars.append(random.choice(string.ascii_letters + string.digits + "!@#$%^&*()-_+="))

        random.shuffle(all_chars)
        return ''.join(all_chars)
    
#---------------------------------------------------PASSWORD VALIDATION CHECKS------------------------------------------------------

    @staticmethod
    def is_valid_password(password):
        if " " in password:
            print("❌ You cannot leave wide spaces in your password.")
        if not (8 <= len(password) <= 15):
            return "❌ The length of your password must be between 8 and 15 characters."
        if not any(char in "!@#$%^&*()_-+=" for char in password):
            return "❌ Your password must contain at least one special character."
        if not any(char.isdigit() for char in password):
            return "❌ Your password must contain at least one digit."
        if not any(char.isalpha() for char in password):
            return "❌ Your password must contain at least one letter."
        return "valid"

    
#---------------------------------------------------------VALID PASSWORD ATTRIBUTE---------------------------------------------------

    def valid_password(self):
        while True:
            print("\n==============================")
            print("      Password Entry")
            print("==============================\n")
            password = getpass(
                "\n🔒 Enter your password below:\n"
                "\n(Note: The password must be between 8 and 15 characters long,\n"
                "and include at least one letter, one number, and one special character.)\n"
                "\nTo Generate a random password enter (y) only:\n >> "
            ).strip()

            if not password:
                print("❌ You cannot leave the space for your password empty.")
                continue

            if password.lower() == "y":
                random_password = self.generate_random_password()
                print(f"🔑 Generated password: {random_password}")
                choice = input("Do you want to use this password? (y/n): ").strip()
                if choice.lower() == "y":
                    return random_password
                elif choice.lower() == "n":
                    continue
                else:
                    print("❌ Please enter a valid input.")
                    continue

            validation_message = self.is_valid_password(password)
            if validation_message == "valid":
                return password
            else:
                print(f"❌ {validation_message}")


#---------------------------------------------------------CHECK FOR PHONE NUMBER----------------------------------------------------

    def valid_phone_no(self):
        while True:
            print("\n==============================")
            print("      Phone Number Entry")
            print("==============================\n")
            no = input("📞 Enter your phone number here.\n(Phone No must be of 11 digits.): ").strip()

            if len(no) == 0:  # Handle empty input
                print("❌ Please enter a phone number.")
            elif len(no) != 11:
                print("❌ Phone number must be of 11 digits.")
            elif not no.isdigit():
                print("❌ Phone number must contain only digits.")
            elif any(char in "!@#$%^&*()_+-=" for char in no):
                print("❌ Please do not use special characters in the phone number.")
            elif any(char.isalpha() for char in no):
                print("❌ Phone number cannot contain alphabets.")
            elif any(char == " " for char in no):
                print("❌ Phone number cannot contain spaces.")
            else:
                return no

            
#-------------------------------------------------------CHECK FOR EMAIL-----------------------------------------------------

    def valid_email(self):
        connection = database.connect()
        connection.isolation_level = None

        while True:
            print("\n==============================")
            print("      Email Entry")
            print("==============================\n")
            email = input("📧 Enter your email here (e.g: abc12@gmail.com): ").strip()

            if database.check_email(connection,email):
                print("❌ The email is already taken.")
            elif not email:
                print("❌ You cannot leave the email portion empty.")
            elif re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
                return email
            elif "@" not in email:
                print("❌ '@' is not found in your email.")
            elif ".com" not in email:
                print("❌ Please add '.com' in your email.")
            elif " " in email:
                print("❌ Please do not add wide spaces in your email.")
            elif not any(char.isdigit() for char in email):
                print("❌ Please add digits in your email.")
            elif not any(char.isalpha() for char in email):
                print("❌ Please add letters in your email.")
            else:
                print("❌ Invalid email.")
            # connection.close()

#-------------------------------------------------SIGNUP-------------------------------------------------------------------------

    def signup(self):
        connection = database.connect()
        connection.isolation_level = None
    
        print("\n==============================")
        print("|            SIGNUP            |")
        print("==============================\n")
        f_name = self.valid_first_name()
        l_name = self.valid_last_name()
        username = self.valid_username()
        password = self.valid_password()
        phone_number = self.valid_phone_no()
        email = self.valid_email()
        add_user(connection,f_name,l_name,email,username,password,phone_number)
        connection.close()

#--------------------------------------LOGIN----------------------------------------------------------------------

    def login(self):
        connection = database.connect()
        connection.isolation_level = None

        while True:
            print("\n==============================")
            print("        User Login")
            print("==============================\n")
            username = input("Username: ").lower().strip()
            password = getpass("Password: ").strip()

            if database.login_validation(connection, username, password):
                print(f"\n✅  Login successful.\n \n---------------Logged in as {username}----------------\n")
                self.active_user = get_user_details(connection,username)
                connection.close()
                return True
            else:
                print("\n❌  Login failed. Invalid username or password. Please try again.\n")
                continue


#-------------------------------------ADMIN LOGIN----------------------------------------------------------------

    def admin_login(self):
        connection = database.connect()
        connection.isolation_level = None
        admin_login(connection)
        self.active_user = 'Admin'
        return True
#--------------------------------------ADMIN MENU-----------------------------------------------------------------

    def display_admin_menu(self):
        self.clear_screen()
        print("\n")
        print("===============================================")
        print("|               Admin Dashboard                |")
        print("===============================================")
        print("|  1. See Users List                           |")
        print("|  2. See Products List                        |")
        print("|  3. Logout                                   |")
        print("===============================================")
        print("\n")

#----------------------------------------DISPLAY USERS-------------------------------------------------------------

    def display_users(self):
        connection = database.connect()
        connection.isolation_level = None
        list_all_users(connection)
        
        while True:
            choice = input("(a) View user details\n(b) Delete user\n(c) Back:\n ").strip().lower()
            if choice == "a":
                self.get_user_details()
                input("Press any key to go back: ")
            elif choice == "b":
                while True:
                    choice2 = input("Enter the number of user you want to delete: ").strip()
                    if choice2.isdigit():
                        user_index = int(choice2) 
                        self.delete_user(user_index)
                        break
                    else:
                        print("\nPlease enter a valid input.")
            elif choice == "c":
                return "Back"
            else:
                print("Please enter a valid input.")

#----------------------------------------------USER DEATILS--------------------------------------------------------

    def get_user_details(self):
        connection = database.connect()
        connection.isolation_level = None
        list_all_users(connection)
        while True:
            number = input("\nEnter the number of User to get details: ").strip()
            if number.isdigit():
                get_user_by_ID(connection,number)
                break
            else:
                print("Please enter a valid input.")

#---------------------------------------------DELETE USER-------------------------------------------------------------

    def delete_user(self, number):
        connection = database.connect()
        connection.isolation_level = None
        while True:
            confirmation = input("Are you sure you want to delete user (y to delete, n to go back): ").strip().lower()
            if confirmation == "y":
                remove_user(connection,number)
                print("\nUser successfully deleted.")
                input("\nPress any key to go back: ")
                return
            elif confirmation == "n":
                return
            else:
                print("\nPlease enter a valid input.")

#------------------------------------------DISPLAY ADMINS--------------------------------------------------------

    def display_admins(self):
        connection = database.connect()
        connection.isolation_level = None
        list_admins(connection)
        while True:
            choice = input("\n(a)Add Admin\n(b)Remove Admin\n(c)Back: ")
            if choice.lower() == "a":
                add_admin(connection)
                print("\nAdmin successfully added!!!")
                input("\nPress any button to go back: ")
            elif choice.lower() == "b":
                while True:
                    choice2 = input("Enter the number of admin you want to delete: ").strip()
                    if choice2.isdigit():
                        choice2 = int(choice2)
                        self.delete_admin(choice2)
                    else:
                        print("\nPlease enter a valid input.")
            elif choice.lower() == "c":
                return "Back"
            else:
                print("Please Enter valid input.")

#------------------------------------------DELETE ADMIN-----------------------------------------------------------

    def delete_admin(self, number):
        connection = database.connect()
        connection.isolation_level = None
        while True:
            confirmation = input("Are you sure you want to delete Admin (y to delete, n to go back): ").strip().lower()
            if confirmation == "y":
                remove_admin(connection,number)
                print("\nAdmin successfully deleted.")
                input("\nPress any key to go back: ")
                break
            elif confirmation == "n":
                return
            else:
                print("Please enter a valid input.")

#------------------------------------------ADMIN RUN--------------------------------------------------------------

    def admin_interface(self):
        connection = database.connect()
        connection.isolation_level = None
        
        while True:
            self.display_admin_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.display_users()
            elif choice == '2':
                System.admin_action_on_products()
            elif choice == '3':
                print("\nLogging out from Admin interface........")
                self.active_user = None
                time.sleep(1)
                break
            else:
                print("\nPlease enter a valid input.")

#--------------------------------------Admin actions on products---------------------------------------------------------------

    @staticmethod
    def admin_action_on_products():
        connection = database.connect()
        connection.isolation_level = None
        while True:
            try:
                choice = int(input("\nEnter your choice: \n(1) Add Product\n(2) Update Product\n(3) View All Products\n(4) Delete Product\n(5) Back\n>>"))
                
                if choice == 1:
                    add_product(connection)
                    print('\nAdding product....')
                    time.sleep(1)
                    print('\nProduct added successfully!!')
                elif choice == 2:
                    update_product(connection)
                    print('\nUpdating product....')
                    time.sleep(1)
                    print('\nProduct updated successfully!!')
                elif choice == 3:
                    print('\nFetching all products....')
                    time.sleep(1)
                    list_all_products(connection)
                elif choice == 4:
                    remove_product(connection)
                    print('\nDeleting product....')
                    time.sleep(0.5)
                    print('\nProduct deleted successfully!!')
                elif choice == 5:
                    return "Back"
                else:
                    print("\nInvalid choice")
            except Exception as e:
                print(f"Error: {e}")


    @staticmethod
    def user_interface(active_user,details):
        connection = database.connect()
        connection.isolation_level = None
        while True:
            print("\n===============================================")
            print("|  1. Proceed To MaketPlace                   |")
            print("|  2. See History                             |")
            print("|  3. View Personal Details                   |")
            print("|  4. Logout                                  |")
            print("===============================================\n")
            print("\n")
            c = input("Enter your choice: ")
            if c.isdigit():
                c = int(c)
                if c == 1:
                    return 'User'
                elif c == 2:
                    print("\nFetching history....")
                    time.sleep(0.5)
                    history = database.get_history(connection,active_user)
                    
                    headers = ["ID", "Username", "Product ID", "Product Name", "Quantity", "Total ($)", "Date"]
                    print(f"{headers[0]:<5} {headers[1]:<15} {headers[2]:<12} {headers[3]:<20} {headers[4]:<10} {headers[5]:<10} {headers[6]:<20}")
                    print("="*95)
                    
                    for record in history:
                        id_, username, product_id, product_name, quantity, total, date = record
                        print(f"{id_:<5} {username:<15} {product_id:<12} {product_name:<20} {quantity:<10} {total:<10.2f} {date:<20}")
                    print('='*95)
                elif c == 3:
                    print(details)
                    input("\nPress any key to continue: ")
                elif c == 4:
                    print("\nExiting the interface.")
                    break
                else:
                    print("\nInvalid choice. Please try again.")
        
                
#--------------------------------------CLIENT CODE---------------------------------------------------------------
                
# system = System()
# system.run()

