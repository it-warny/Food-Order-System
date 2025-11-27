
# Create a database:
inventory = {"laptop": 8, "smart tv": 12, "refrigerator": 5, "wardrobe": 110.25} # STR / INT
prices = {"laptop": 345.50, "smart tv": 228.90, "refrigerator": 495.20, "wash machine": 195.10} # STR / FLOAT


# Create a function and the logic:
def process_purchase(item_name, quantity):
    if item_name not in prices:
        return "Not for sale"
    elif item_name not in inventory:
        return "Out of stock"
    elif inventory[item_name] >= quantity:
        return "Not enough stock"
    else:
        return prices[item_name] * quantity


# Testing the code:
print(f"Is the item for sale? \n{process_purchase('wardrobe', 8)}") # Should be not for sale
print(f"\nDo we have it? \n{process_purchase('wash machine', 8)}") # Should be out of stock
print(f"\nDo we have enough? \n{process_purchase('smart tv', 15)}") # Should be not enough stock
print(f"\nIf all gates are passed, calculate: \n{process_purchase('laptop', 4):.2f}€") # Should be fine




