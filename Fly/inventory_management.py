'''
management of an invertory, for ex- in an ecommerce site
'''

# managing an inventory
inventory = ["apples", "bananas", "oranges", "grapes"]

# adding an item
inventory.append("strawberries")

# removing item that is out of stock
inventory.remove("oranges")

#checking if an item is in stock
item = "grapes"
if item in inventory:
    print(f"{item} are in stock.")
else:
    print(f"{item} are out of stock.")


# printing the inventory
print("Inventory List: ")
for item in inventory:
    print(f"- {item}")