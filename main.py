# main.py
from models.Backup import System
from models.MarketPlace import Marketplace
from models.Cart import Cart
from models.Order2 import BasicOrder
from models.History import History
from models.db_functions import loadAllProducts,update_marketplace_products
from models import database
import time


connection = database.connect()
database.create_product_tables(connection)

def main():
    system = System()
    #checks if the user is an admin or a customer , in case of admin it will return 
    if system.run() == 'User': pass
    elif system.run() == 'Admin': return
    else: return
    
    # Step 1: Initialize the Marketplace
    marketplace = Marketplace()

    # Step 2: Add initial products to the marketplace
    
    #Loads the products from the database into the marketplace
    loadAllProducts(connection,marketplace)

    # Step 3: Initialize an empty cart
    cart = Cart(marketplace)

    # Step 4: Display a menu for user interactions
    while True:
        print("\nWelcome to the Marketplace\n----------------------------------------")
        print("\n1. List all products")
        print("2. Search for products")
        print("3. Add product to cart")
        print("4. View cart")
        print("5. Checkout")
        print("6. Exit\n----------------------------------------")
        
        choice = input("\nPlease choose an option: ")

        # Validate user input to ensure it's a number between 1 and 6
        if not choice.isdigit() or not 1 <= int(choice) <= 6:
            print("Invalid choice. Please enter a number between 1 and 6.")
            continue  # Prompt the menu again

        choice = int(choice)

        if choice == 1:
            # List all products
            print("\nAvailable Products:")
            for product in marketplace.list_products():
                qty = 'Available' if product.product_quantity != 0 else 'Not Available'
                print(f"\n{product.product_id}. {product.product_name}, Price: ${product.product_price:.2f}, Availability: {qty}")

        elif choice == 2:
            # Search for products
            keyword = input("\nEnter keyword to search for: ")
            results = marketplace.search_products(keyword)
            if results:
                print("\nSearch Results:")
                for product in results:
                    # Here , what we are doing is that we are checking if the product is available or not , if it not available then we will still show it top the user but not stock will be shown as 'Not Available'
                    qty = 'Available' if product.product_quantity != 0 else 'Not Available'
                    print(f"\n{product.product_id}. {product.product_name} Price: ${product.product_price:.2f}, Availability: {qty}")
            else:
                print("\nNo products found matching your search.")

        elif choice == 3:
            # Add product to cart
            while True:
                try:
                    for product in marketplace.list_products():
                        # Here , what we are doing is that we are checking if the product is available or not , if it not available then we will not show it to the user
                        if product.product_quantity == 0 : continue
                        else: qty = 'Available'
                        print(f"\n{product.product_id}. {product.product_name}, Price: ${product.product_price:.2f}, Availability: {qty}")
                    product_id = int(input("\nEnter the product NUMBER to add to the cart:\n(0)Back\n>>"))
                    if product_id == 0 :
                        break
                    quantity = int(input("\nEnter the quantity: "))

                    product = marketplace.get_product(product_id)
                    if product:
                        if product.product_quantity >= quantity:
                            cart.add_product(product, quantity)
                            product.product_quantity = product.product_quantity - quantity
                            print(f"\nAdded {quantity} units of {product.product_name} to the cart.")
                            break
                        else:
                            print('Low Stock!.')
                    else:
                        print("\nProduct not found. :( ")
                except ValueError:
                    print("\nInvalid input. Please enter valid numbers for product ID or quantity.")
                except Exception as e:
                    print(f"Error: {e}")

        elif choice == 4:
            # View cart
            while True:
                
                print("\nCart Contents:")
                for product, quantity in cart.get_cart().items():
                    if quantity == 0 : continue
                    print(f"\n{product.product_id}  {product.product_name}: {quantity} units\n")
                    
                if len(cart.get_cart()) == 0 : print('\n--NILL--')
                
                print(f"\nTotal price: ${cart.get_total_price():.2f}\n")
                prompt = input('\n(b)Back\n(r)Remove Product from cart\n>> ')
                if prompt == 'b':
                    break
                elif prompt == 'r':
                    product_id = int(input("\nEnter the product NUMBER to remove from the cart:\n(0)Back\n>>"))
                    if product_id == 0:
                        break
                    quantity = int(input("\nEnter the quantity: "))
                    quantity = 0 if quantity < 0 else quantity
                    product = marketplace.get_product(product_id)
                    if product:
                        cart.remove_product(product, quantity)
                        product.product_quantity = product.product_quantity + quantity
                        print(f"\nRemoved {quantity} units of {product.product_name} from the cart.")
                        break
                else:
                    print('\nInvalid Input')

        elif choice == 5:
            database.create_users_history_table(connection)
            if cart.is_empty():
                print("\nYour cart is empty. Please add some products first.")
                continue
            order = BasicOrder(cart,system.active_user.get_username())
            # Checkout 
            order.run()
            print("\nChecking out...")
            #writing the history of the user
            for product, quantity in cart.get_cart().items():
                active_user = system.active_user.get_username()
                database.write_history(connection, active_user, str(product.product_id), product.product_name, str(quantity), product.product_price * quantity, time.strftime("%Y-%m-%d %H:%M:%S"))
            database.write_history(connection, '-', '-', '-', '-', cart.get_total_price(), '-')
            print("\nThank you for your purchase!\n")
            cart.clear_cart()
            update_marketplace_products(connection,marketplace) # Updates the products in the database after CHECKOUT

        elif choice == 6:
            # Exit the application
            print("\nExiting the marketplace.......")
            time.sleep(1)
            connection.close()
            print('\n------------------------Goodbye!----------------------------')
            break

if __name__ == "__main__":
    main()
