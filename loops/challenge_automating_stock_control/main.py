# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100
print("Processing started")
for item in inventory:
    print(f'Processing {item}')
    current_stock = inventory[item][0]
    print(f'Current stock: {current_stock}')
    minimum_stock = inventory[item][1]
    print(f'Minimum stock: {minimum_stock}')
    restock_quantity = inventory[item][2]
    print(f'Restock quantity: {restock_quantity}')
    on_sale = inventory[item][3]
    print(f'On sale: {on_sale}')
    #print("Processing")
    while current_stock < minimum_stock:
        current_stock += restock_quantity
        inventory[item][0] = current_stock
    if current_stock > discount_threshold and on_sale != True:
        inventory[item][3] = True
    print(inventory)
    print("Processing completed")