def exclusive_products(inventory1, inventory2):
    # changes the case of all items in both inventories to uppercase to ensure case insensitive comparison
    inv1 = [item.upper() for item in inventory1]
    inv2 = [item.upper() for item in inventory2]
    # This is finding unique items in both inventories connverting them to sets to remove duplicates, then converting them back to sorted lists and returning them as a tuple
    unique_items1 = set(inv1) - set(inv2)
    unique_items2 = set(inv2) - set(inv1)
    return (sorted(list(unique_items1)), sorted(list(unique_items2)))

inventory1 = ["Shirt", "Jeans", "Hat"]
inventory2 = ["jeans", "Belt", "Boots"]
print(exclusive_products(inventory1, inventory2))
# Expected output: (['HAT', 'SHIRT'], ['BELT', 'BOOTS'])

inventory1 = ["T-Shirt", "hoodie", "Backpack"]
inventory2 = ["Backpack", "Hoodie", "t-shirt"]
print(exclusive_products(inventory1, inventory2))
# Expected output: ([], [])

inventory1 = []
inventory2 = ["Dress", "Skirt", "Coat"]
print(exclusive_products(inventory1, inventory2))
# Expected output: ([], ['COAT', 'DRESS', 'SKIRT'])
