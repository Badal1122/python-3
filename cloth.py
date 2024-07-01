# '''Create a dictionary-based mini project in Python to manage an inventory in stock. 
# The user should have options to add new items, buy items, change the price of items, 
# and update the inventory of current items. There should also be a total sales variable 
# that is initially set to 0. The project should handle inventory, price, and count. 
# The project should be broken down into steps with clear instructions for each step. 
# Each step should be pushed to GitHub.

# 1. Create a new GitHub repository and set up a new Python project.

# 2. Define the inventory dictionary to hold item data and a variable for total sales.

# 3. Create a `main` function to run the program and print a welcome message.

# 4. Create a function `add_item` to add new items to the inventory with a specified name, price, and count.

# 5. Update the `main` function to include a menu option for adding new items.

# 6. Commit the changes to GitHub.

# 7. Create a function `buy_item` to handle buying items from the inventory, updating the item count and total sales.

# 8. Update the `main` function to include a menu option for buying items.

# 9. Commit the changes to GitHub.

# 10. Create a function `change_price` to update the price of an existing item in the inventory.

# 11. Update the `main` function to include a menu option for changing item prices.

# 12. Commit the changes to GitHub.

# 13. Create a function `display_inventory` to print the current state of the inventory and total sales.

# 14. Update the `main` function to include a menu option for displaying the inventory.

# 15. Commit the changes to GitHub.

# 16. Create a function `update_inventory` to update the count of an existing item in the inventory.

# 17. Update the `main` function to include a menu option for updating the inventory count of existing items.

# 18. Commit the changes to GitHub.

# 19. Review and refactor the code if necessary. Add comments and documentation to explain the functionality.

# 20. Add a final commit to GitHub with any refinements and the completed project.'''

print("Welcome to Cloth Inventory Management system:")
inventory = {
     "shirt": {"price": 25, "count": 150},
    "jeans": {"price": 50, "count": 100},
    "jacket": {"price": 100, "count": 75},
    "dress": {"price": 70, "count": 60},
    "skirt": {"price": 40, "count": 80},
}
for key,value in inventory.items():
    print(f"{key}:{value}")
def add_item():
    name = input("Enter the name of the item: ")
    price = int(input("Enter the price of the item: "))
    count = int(input("Enter the count of the item: "))
    inventory[name] = {"price": price, "count": count}
    print(inventory)
def buy_item():
    name = input("Enter the name of the item: ")
    count = int(input("Enter the count of the item: "))
    if name in inventory:
        if inventory[name]["count"] >= count:
            inventory[name]["count"] -= count
            print("Item purchased successfully")
        else:
            print("Item not available in sufficient quantity")
    else:
        print("Item not available")

def change_price():
    name = input("Enter the name of the item: ")
    price = int(input("Enter the new price of the item: "))
    if name in inventory:
        inventory[name]["price"] = price
        print("Price updated successfully")
    else:
        print("Item not available")
def update_inventory():
    name = input("Enter the name of the item: ")
    count = int(input("Enter the new count of the item: "))
    if name in inventory:
        inventory[name]["count"] = count
        print("Count updated successfully")
    else:
        print("Item not available")
def display_inventory():
    total_sale = 0
    print("Inventory:")
    for key, values in inventory.items():
        print(f"{key} : {values['count']}")
        total_sale += values['price'] * values['count']
    print(f"Total sales: {total_sale}")
