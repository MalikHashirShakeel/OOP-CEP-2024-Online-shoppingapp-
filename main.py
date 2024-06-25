# main.py

from models.Product import Product
from models.MarketPlace import Marketplace
from models.Cart import Cart

def main():
    # Step 1: Initialize the Marketplace
    marketplace = Marketplace()

    # Step 2: Add initial products to the marketplace
    products = [
        Product(1, "Lenovo Legion", "Lenovo Legion", 1500.0, 10),
        Product(2, "S22 ULTRA", "S22 ULTRA", 800.0, 20),
        Product(3, "HperX Cloud Alpha Wireless", "HperX Cloud Alpha Wireless", 200.0, 50),
        Product(4, "HyperX Alloy Origins", "HyperX Alloy Origins", 300.0, 15)
    ]
    
    for product in products:
        marketplace.add_product(product)

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
                print(f"\n{product.product_id}. {product.product_name} Price: ${product.product_price:.2f}, Stock: {product.product_quantity}")

        elif choice == 2:
            # Search for products
            keyword = input("\nEnter keyword to search for: ")
            results = marketplace.search_products(keyword)
            if results:
                print("\nSearch Results:")
                for product in results:
                    qty = 'Available' if product.product_quantity != 0 else 'Not Available'
                    print(f"\n{product.product_id}. {product.product_name}, Price: ${product.product_price:.2f}, Availability: {qty}")
            else:
                print("\nNo products found matching your search.\n")

        elif choice == 3:
            # Add product to cart
            try:
                for product in marketplace.list_products():
                    print(f"\n{product.product_id}. {product.product_name}, Price: ${product.product_price:.2f}, Stock: {product.product_quantity}")
                product_id = int(input("\nEnter the product ID to add to the cart: "))
                quantity = int(input("\nEnter the quantity: "))

                product = marketplace.get_product(product_id)
                if product:
                    cart.add_product(product, quantity)
                    print(f"\nAdded {quantity} units of {product.product_name} to the cart.")
                else:
                    print("\nProduct not found. :( ")
            except ValueError:
                print("\nInvalid input. Please enter valid numbers for product ID and quantity.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == 4:
            # View cart
            print("\nCart Contents:")
            for product, quantity in cart.get_cart().items():
                print(f"\n{product.product_name}: {quantity} units\n")
                
            if len(cart.get_cart()) == 0 : print('\n--NILL--')
            
            print(f"\nTotal price: ${cart.get_total_price():.2f}\n")

        elif choice == 5:
            # Checkout (simplified)
            print("\nChecking out...")
            for product, quantity in cart.get_cart().items():
                print(f"\n{quantity} units of {product.product_name} - ${product.product_price * quantity:.2f}\n")
            print(f"\nTotal price to pay: ${cart.get_total_price():.2f}\n")
            print("\nThank you for your purchase!\n")
            cart.clear_cart()

        elif choice == 6:
            # Exit the application
            print("\nExiting the marketplace. Goodbye!\n")
            break

if __name__ == "__main__":
    main()
