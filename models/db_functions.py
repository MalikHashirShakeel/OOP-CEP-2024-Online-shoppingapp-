from . import database
from .User_class import User
from .Product import Product
import time
import bcrypt
from getpass import getpass
def main():
    
    connection = database.connect()
    connection.isolation_level = None
    database.create_product_tables(connection)
    database.create_users_table(connection)
    
    while True:
        choice = int (input('\nEnter your choice : \n(0)Back\n>>'))
        if choice == 0: break
        if choice == 1:
            add_product(connection)
        elif choice==2:
            update_product(connection)
        elif choice==3: 
            loadAllProducts(connection)
        elif choice==4:
            search_product_by_name(connection)
        elif choice==5:
            remove_product(connection)
        elif choice==6:
            list_all_products(connection)
        else:
            print('\nInvalid choice')
            
 #Admin exclusive function
def add_product(connection):
    while True:
        try:
            name = input('\nEnter name of product : ').upper()
            if name:
                pass
            else:
                print("Name cannot be empty\nTry again\n")
                continue
            description = input('\nEnter description of product : ')
            if description:
                pass
            else:
                print("Description cannot be empty\nTry again\n")
                continue
            price = float(input('\nEnter price of product : '))
            if price:
                pass
            else:
                print("Price cannot be empty\nTry again\n")
                continue
            quantity = int(input('\nEnter quantity of product : '))
            if quantity != 0:
                pass
            else:
                print("Quantity cannot be Zero\nTry again\n")
                continue
        except Exception as e:
            print(f'Error : {e}')
            continue
        else:
            database.add_product(connection, name, description, price, quantity)
            break
        # rating = float(input('\nEnter rating of product : '))
        
#Admin exclusive function
def remove_product(connection):
    products = database.get_all_products(connection)
    for product in products:
        print(f'{product[0]} : {product[1]}')
    name = input('\nEnter name of product to remove : ')
    database.remove_product(connection, name)
    
#Admin exclusive function 
def update_product(connection):
    products = database.get_all_products(connection)
    for product in products:
        print(f'\n{product[0]} : {product[1]} Price: {product[3]} Quantity: {product[4]}')
    try:  
        product_id = int(input('\nEnter number of product to update : \n(0)Back\n>>'))
        if product_id == 0:
            return
        description = input('\nEnter description of product : ')
        if description:
            pass
        else:
            print("Description cannot be empty\nTry again\n")
            return
        price = float(input('\nEnter price of product : '))
        if price:
            pass
        else:
            print("Price cannot be empty\nTry again\n")
            return
        quantity = int(input('\nEnter quantity of product : '))
        if quantity != 0 :
            pass
        elif not (quantity < 0) : pass
        else:
            print("Quantity cannot be Zero\nTry again\n")
            return
    except Exception as e:
        print(f'Error : {e}')
        return
    database.update_product_in_db(connection, product_id, product[1], description, price, quantity)

#function to load all products from database to the Marketplace , Marketplace exclusive fuction
def loadAllProducts(connection,marketplace):
    products = database.get_all_products(connection)
    for product in products:
        product_id, name, description, price, stock = product
        product = Product(product_id, name, description, price, stock )
        marketplace.add_product(product)
        
        
def search_product_by_name(connection):
    
    name = input('\nEnter name of product to search : ').upper()
    print('Searching......')
    products = database.search_product_by_name(connection, name)
    time.sleep(1)
    for product in products:
        print(product)
        
def update_all_products(connection):
    products = database.get_all_products(connection)
    for product in products:
        database.update_product(connection, product[1], product[2], product[3], product[4], product[5])

def list_all_products(connection):
    products = database.get_all_products(connection)
    for product in products:
        print(f'     ID      :       NAME     |  DESCRIPTION |    PRICE     |   QUANTITY  ')
        print(f'\n{product[0]} : {product[1]} | {product[2]} | {product[3]} | {product[4]}')

#<---------------------------------Marketplace exclusive function------------------------------------------------------>

def update_marketplace_products(connection, marketplace):
    """
    Retrieves products from the marketplace and updates them in the database.
    """
    try:
        # Retrieve the list of products from the marketplace
        products = marketplace.list_products()
        
        # Iterate through each product and update it in the database
        for product in products:
            product_id = product.product_id
            name = product.product_name
            description = product.product_description
            price = product.product_price
            quantity = product.product_quantity
            
            # Attempt to convert the price to a float
            try:
                price = float(price)
            except ValueError as e:
                print(f"Invalid price for product ID {product_id}: {price}. Setting price to 0.0. Error: {e}")
                price = 0.0
            
            # Update the product in the database
            database.update_product_in_db(connection, product_id, name, description, price, quantity)
        
        print("Finished updating all marketplace products.")

    except Exception as e:
        print(f"Error while updating marketplace products: {e}")
        
#<------------------users queries------------------->|
    
def add_user(connection,f_name,l_name,email,username,password,phone_no):
    if database.check_email(connection,email):
        print('\nEmail already exists')
        return
    if database.username_validation(connection,username):
        print('\nUsername already exists')
        return
    else:
        database.add_user(connection,f_name,l_name,email,username,password,phone_no)
    
def user_login(connection,username,password):
    if database.user_login(connection,username,password):
        return True
    else:
        return False

def get_user_details(connection,username):
    user = database.get_user_details(connection,username)
    user_id,f_name,l_name,email,username,password,phone_number = user
    return User(f_name,l_name,username,email,password,phone_number)

def list_all_users(connection):
    users = database.list_users(connection)
    for user in users:
        print(f'{user[0]} : {user[4]}')

#<------------------Admin queries------------------->|
    
def get_user_by_ID(connection,id):
    user = database.get_user_by_ID(connection,id)
    print(f'{user[0]} : {user[1]} | {user[2]} | {user[3]} | {user[4]} | {user[6]}')
    
def remove_user(connection,id):
    database.remove_user(connection,id)
    
def list_admins(connection):
    admins = database.list_admins(connection)
    for admin in admins:
        for _ in admin:
            print(f'{admin[0]} : {admin[1]}')

def remove_admin(connection,id):
    database.remove_admin(connection,id)
    
def add_admin(connection):
    while True:
        print("\n==============================")
        print("           Add Admin            ")
        print("==============================\n")
        username = input("Enter admin username: ").lower().strip()
        
        # Check if the username already exists
        if username_exists(connection, username):
            print("\n⚠️  Username is already taken! Please choose another username.\n")
            continue
        
        password = getpass("Enter admin password: ").strip()
        confirm_password = getpass("Confirm password: ").strip()

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
        except Exception as e:
            print(f"\n❌  Error adding admin user: {e}\n")
            continue
        
def username_exists(connection, username):
    with connection:
        result = connection.execute(database.CHECK_ADMIN_USERNAME, (username,)).fetchone()
        return result and result[0] > 0  # Returns True if username exists
    
def admin_login(connection):
    while True:
        print("\n==============================")
        print("        Admin Login")
        print("==============================\n")
        username = input("\nAdmin Username: ").lower().strip()
        password = getpass("Admin Password: ").strip()  

        if validate_admin_credentials(connection, username, password):
            print(f"\n✅  Login successful.\n--------------- Welcome, {username}!---------------")
            print('\nLoading Admin Panel....')
            time.sleep(1)
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
    


if __name__ == "__main__":
    main()