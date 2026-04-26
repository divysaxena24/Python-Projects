import copy

def create_inventory():
    return [
        {
            "item": "Laptop",
            "details": {"price": 50000, "stock": 10, "supplier": {"rating": 4.5}}
        },
        {
            "item": "Phone",
            "details": {"price": 20000, "stock": 25, "supplier": {"rating": 4.0}}
        }
    ]

def apply_discount(data, index):
    for i in range(len(data)):
        if i == index:
            data[i]["details"]["price"] *= 0.9
            data[i]["details"]["stock"] += 5

def compare_data(original, modified):
    changed = 0
    unchanged = 0
    for i in range(len(original)):
        if original[i] != modified[i]:
            changed += 1
        else:
            unchanged += 1
    return (changed, unchanged)

inventory = create_inventory()

shallow_copy = inventory.copy()
deep_copy = copy.deepcopy(inventory)

index = 570 % len(inventory)

apply_discount(shallow_copy, index)
apply_discount(deep_copy, index)

print("Original Inventory:")
print(inventory)

print("\nShallow Copy:")
print(shallow_copy)

print("\nDeep Copy:")
print(deep_copy)

print("\nComparison (Original vs Shallow):")
print(compare_data(inventory, shallow_copy))

print("\nComparison (Original vs Deep):")
print(compare_data(inventory, deep_copy))