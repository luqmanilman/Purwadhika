from tabulate import tabulate

welcome_admin = '''
    Welcome Admin Lq's Bookstore
            
Menu List :
1. View Stock
2. Add Stock
3. Remove Stock
4. Update Stock
5. Sort Stock
6. Search Item
7. Back to User Choice
8. Exit Program
'''

welcome_user = '''
    Welcome User Lq's Bookstore

Menu List :
1. View Stock
2. Buy Item
3. Sort Stock
4. Search Item
5. Back to User Choice
6. Exit Program
'''

# Initial Items
Store_items = [
    {'Name': 'Novel', 'Stock': 15, 'Price': 95000},
    {'Name': 'Comics', 'Stock': 20, 'Price': 65000},
    {'Name': 'Magazine', 'Stock': 10, 'Price': 25000},
    {'Name': 'Pencil', 'Stock': 30, 'Price': 5000},
    {'Name': 'Notebook', 'Stock': 25, 'Price': 20000},
    {'Name': 'Eraser', 'Stock': 45, 'Price': 3000},
    {'Name': 'Pen', 'Stock': 15, 'Price': 10000},
    {'Name': 'Marker', 'Stock': 20, 'Price': 15000},
    {'Name': 'Ruler', 'Stock': 10, 'Price': 5000},
    {'Name': 'Stapler', 'Stock': 10, 'Price': 20000}
]

def display_menu(is_admin):
    if is_admin:
        print(welcome_admin)
    else:
        print(welcome_user)

def display_item_list(items):
    headers = ["Index", "Name", "Stock", "Price"]
    data = [[i, item['Name'], item['Stock'], f"Rp {item['Price']}"] for i, item in enumerate(items)]
    print(tabulate(data, headers=headers, tablefmt="heavy_outline"))
#Add item Function
def add_item():
    name_item = input('Enter the name of item (or type "cancel" to cancel): ')
    
    # Check if the user wants to cancel
    if name_item.lower() == "cancel":
        print("Adding item canceled.")
        return
    
    try: #Checking the input must be integer
        stock = int(input('Enter the amount of Stock: '))
        if stock < 0:
            print("Stock must be greater than or equal to 0.")
            return
        price = int(input('Enter the correct Price: '))
        
        # Check if the item already exists (case-insensitive), then add to existing stock
        existing_stock = None
        for item in Store_items:
            if item['Name'].lower() == name_item.lower():
                existing_stock = item
                break
        
        if existing_stock:
            existing_stock['Stock'] += stock
            print(f"{name_item} successfully added to existing stock!")
        else:
            Store_items.append({'Name': name_item, 'Stock': stock, 'Price': price})
            print("Item successfully added!")
    except ValueError:
        print("Invalid input! Stock and Price must be integers.")

def remove_item(): #Remove item function
    display_item_list(Store_items)
    choice = input('Enter the index or name of the item you want to delete: ')
    
    try: #Trying to delete by index
        index = int(choice)
        if 0 <= index < len(Store_items):
            del Store_items[index]
            print('Item successfully deleted by index!')
        else:
            print("Index out of range! Please enter a valid index.")
    except ValueError: #Deleted by name
        found_items = [item for item in Store_items if item['Name'].lower() == choice.lower()]
        if found_items:
            if len(found_items) == 1:
                Store_items.remove(found_items[0])
                print(f"{choice} successfully deleted by name!")
            else:
                print("Multiple items found with the same name. Please specify further.")
        else:
            print("No item found with that name.")

def update_item(): #Update function
    display_item_list(Store_items)
    choice = input('Enter the index or name of the item you want to update: ')
    
    try:
        index = int(choice)
        if 0 <= index < len(Store_items):
            while True:
                new_stock = int(input('Enter the new amount of Stock (input 99 to cancel): '))
                if new_stock == 99:
                    print("Update canceled.")
                    break
                elif new_stock < 0:
                    print("Stock must be greater than or equal to 0.")
                else:
                    new_price = int(input('Enter the new Price: '))
                    Store_items[index]['Stock'] = new_stock
                    Store_items[index]['Price'] = new_price
                    print("Item successfully updated!")
                    break
        else:
            print("Index out of range! Please enter a valid index.")
    except ValueError:
        found_items = [item for item in Store_items if item['Name'].lower() == choice.lower()]
        if found_items:
            if len(found_items) == 1:
                while True:
                    new_stock = int(input('Enter the new amount of Stock (input 99 to cancel): '))
                    if new_stock == 99:
                        print("Update canceled.")
                        break
                    elif new_stock < 0:
                        print("Stock must be greater than or equal to 0.")
                    else:
                        new_price = int(input('Enter the new Price: '))
                        found_items[0]['Stock'] = new_stock
                        found_items[0]['Price'] = new_price
                        print(f"{choice} successfully updated by name!")
                        break
            else:
                print("Multiple items found with the same name. Please specify further.")
        else:
            print("No item found with that name.")

def buy_item(): #Buy function
    display_item_list(Store_items)
    cart = [] #empty/blank list cart
    total_price = 0

    while True:
        choice = input('Enter index or name of the item you want to buy (input 99 to finish Shopping): ')
        if choice == '99':
            break
        try: #Checking for value must greater or equal to 0
            index = int(choice)
            if 0 <= index < len(Store_items):
                while True:
                    total_items = int(input(f'Enter Stock {Store_items[index]["Name"]}: '))
                    if total_items < 0:
                        print("Stock must be greater than or equal to 0.")
                    else:
                        break
                if total_items <= Store_items[index]['Stock']:
                    total_price += Store_items[index]['Price'] * total_items
                    Store_items[index]['Stock'] -= total_items
                    # Check if the item is already in the cart
                    existing_item_index = next((i for i, item in enumerate(cart) if item['Name'] == Store_items[index]['Name']), None)
                    if existing_item_index is not None:
                        cart[existing_item_index]['total_items'] += total_items
                    else:
                        cart.append({'Name': Store_items[index]['Name'], 'total_items': total_items})
                else:
                    print('Stock is not enough!')
            else:
                print('Index not valid')
        except ValueError:
            found_items = [item for item in Store_items if item['Name'].lower() == choice.lower()]
            if found_items:
                if len(found_items) == 1:
                    while True:
                        total_items = int(input(f'Enter Stock {found_items[0]["Name"]}: '))
                        if total_items < 0:
                            print("Stock must be greater than or equal to 0.")
                        else:
                            break
                    if total_items <= found_items[0]['Stock']:
                        total_price += found_items[0]['Price'] * total_items
                        found_items[0]['Stock'] -= total_items
                        # Check if the item is already in the cart
                        existing_item_index = next((i for i, item in enumerate(cart) if item['Name'] == found_items[0]['Name']), None)
                        if existing_item_index is not None:
                            cart[existing_item_index]['total_items'] += total_items
                        else:
                            cart.append({'Name': found_items[0]['Name'], 'total_items': total_items})
                    else:
                        print('Stock is not enough!')
                else:
                    print("Multiple items found with the same name. Please specify further.")
            else:
                print("No item found with that index or name.")

    # Print cart content
    for item in cart:
        print(f"{item['Name']}: {item['total_items']}")
    
    print(f"\nTotal purchase price: Rp {total_price}")

    # Payment
    while True:
        payment = get_integer_input("Enter the amount you are paying: Rp ")
        if payment >= total_price:
            break
        else:
            print("The amount you entered is insufficient. Please enter a sufficient amount.")

    # Calculate change
    change = payment - total_price
    if change > 0:
        print(f"Thank you! Your change is: Rp {change}")
    else:
        print("Thank you!")
#Function for sorting item
def sort_items():
    sort_choice = input("Sort Stock (name, stock, price): ").lower()
    if sort_choice == "name": #Sorting by name
        sub_sort_choice = input("Select order (1. A-Z, 2. Z-A): ")
        if sub_sort_choice == "1":
            sorted_items = sorted(Store_items, key=lambda x: x['Name'])
        elif sub_sort_choice == "2":
            sorted_items = sorted(Store_items, key=lambda x: x['Name'], reverse=True)
        else:
            print("Invalid choice.")
            return
    elif sort_choice == "stock": #Sorting by stock
        sub_sort_choice = input("Select order (1. Ascending, 2. Descending): ")
        if sub_sort_choice == "1":
            sorted_items = sorted(Store_items, key=lambda x: x['Stock'])
        elif sub_sort_choice == "2":
            sorted_items = sorted(Store_items, key=lambda x: x['Stock'], reverse=True)
        else:
            print("Invalid choice.")
            return
    elif sort_choice == "price": #Sorting by price
        sub_sort_choice = input("Select order (1. Ascending, 2. Descending): ")
        if sub_sort_choice == "1":
            sorted_items = sorted(Store_items, key=lambda x: x['Price'])
        elif sub_sort_choice == "2":
            sorted_items = sorted(Store_items, key=lambda x: x['Price'], reverse=True)
        else:
            print("Invalid choice.")
            return
    else:
        print("Invalid choice.")
        return
    display_item_list(sorted_items)

#Function for search the item in the table 
def search_item_by_name():
    search_term = input("Enter the name of the item you want to search for: ").lower()
    found_items = [item for item in Store_items if search_term in item['Name'].lower()] 
    if found_items:
        display_item_list(found_items)
    else:
        print("No items found with that name.")

def search_item():
    search_item_by_name()

#function for checking integer
def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Invalid input! Please enter a non-negative integer.")
            else:
                return value
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

def main():
    while True:
        while True:
            user_type = input('''
Welcome To Lq's Bookstore


Are you an Admin or a User? (Admin/User): ''').lower()
            if user_type == "admin":
                while True:
                    password = input("Enter password for admin access: ")
                    if password == "admin":
                        is_admin = True
                        break
                    else:
                        print("Incorrect password! Please try again.")
                break  # Exit the admin user selection loop
            elif user_type == "user":
                is_admin = False
                break  # Exit the admin user selection loop
            else:
                print("Invalid input! Please enter either 'Admin' or 'User'.")

        while True:
            display_menu(is_admin)
            if is_admin:
                pilihan = get_integer_input('Enter your menu choice : ')
                if pilihan == 1:
                    display_item_list(Store_items) # Call display item for both admin and user
                elif pilihan == 2:
                    add_item() #Call add item function for admin
                elif pilihan == 3:
                    remove_item() #call remove function for admin
                elif pilihan == 4:
                    update_item() #Call update function for admin
                elif pilihan == 5:
                    sort_items() #Call Sort function for both admin and user
                elif pilihan == 6:
                    search_item()  # Call the search_item function for both admin and user
                elif pilihan == 7:
                    break  # Go back to the admin/user selection
                elif pilihan == 8:
                    print('Thank you for using this program!')
                    return
                else:
                    print('Invalid choice')
            else:
                pilihan = get_integer_input('Enter your menu choice : ')
                if pilihan == 1:
                    display_item_list(Store_items) # Call display item for both admin and user
                elif pilihan == 2:
                    buy_item() # Call buy function for user 
                elif pilihan == 3:
                    sort_items() #Call Sort function for both admin and user
                elif pilihan == 4:
                    search_item()  # Call the search_item function for both admin and user
                elif pilihan == 5:
                    break # Go back to the admin/user selection
                elif pilihan == 6:
                    print('Thank you for using this program!')
                    return
                else:
                    print('Invalid choice')
main()
