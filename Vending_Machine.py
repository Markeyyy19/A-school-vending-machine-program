# A school Vending Machine Program

# Products: [name, price, stock]
products = {
    
    # Hot Drinks
    "A1": {"name": "Coffee", "price": 4.00, "stock": 10},
    "A2": {"name": "Tea", "price": 3.00, "stock": 8},
    "A3": {"name": "Hot Chocolate", "price": 3.75, "stock": 6},
    
    # Drinks
    "B1": {"name": "Water", "price": 2.00, "stock": 15},
    "B2": {"name": "Coke", "price": 4.00, "stock": 12},
    "B3": {"name": "Sprite", "price": 6.00, "stock": 10},
    
    # Candy
    "C1": {"name": "Snickers", "price": 5.65, "stock": 20},
    "C2": {"name": "KitKat", "price": 4.95, "stock": 18},
    "C3": {"name": "Toblerone", "price": 5.65, "stock": 15},
    
    # Snacks
    "D1": {"name": "Biscuit", "price": 6.55, "stock": 25},
    "D2": {"name": "Croissant", "price": 2.55, "stock": 20},
    "D3": {"name": "Oreo", "price": 1.55, "stock": 15}
}
# This will suggest another item to be paired with the item that is purchased
suggestions = {
    "Coffee": "Croissant",
    "Tea": "Biscuits",
    "Coke": "Biscuit",
    "Water": "Croissant",
    "Sprite": "Oreo",
}


def show_menu():
    print("\n" + "=" * 40)
    print("      SCHOOL VENDING MACHINE")
    print("=" * 40)
    
    # Hot Drinks Category
    print("\n    HOT DRINKS    ")
    for code in ["A1", "A2", "A3"]:
        name = products[code]["name"]
        price = products[code]["price"]
        stock = products[code]["stock"]
        status = "Available" if stock > 0 else "OUT OF STOCK"
        print(code + ": " + name + " - " + str(price) + " SAR (" + status + ")")
    
    # Drinks Category
    print("\n    COLD DRINKS    ")
    for code in ["B1", "B2", "B3"]:
        name = products[code]["name"]
        price = products[code]["price"]
        stock = products[code]["stock"]
        status = "Available" if stock > 0 else "OUT OF STOCK"
        print(code + ": " + name + " - " + str(price) + " SAR (" + status + ")")
    
    # Candy Category
    print("\n    CANDY    ")
    for code in ["C1", "C2", "C3"]:
        name = products[code]["name"]
        price = products[code]["price"]
        stock = products[code]["stock"]
        status = "Available" if stock > 0 else "OUT OF STOCK"
        print(code + ": " + name + " - " + str(price) + " SAR (" + status + ")")
    
    # Snacks Category
    print("\n    SNACKS    ")
    for code in ["D1", "D2", "D3"]:
        name = products[code]["name"]
        price = products[code]["price"]
        stock = products[code]["stock"]
        status = "Available" if stock > 0 else "OUT OF STOCK"
        print(code + ": " + name + " - " + str(price) + " SAR (" + status + ")")
    
    print("\n" + "=" * 40)

print("Welcome to the School Vending Machine!")

while True:
    show_menu()
    
    code = input("\nEnter code (or E to quit): ")
    code = code.upper()
    
    if code == "Q":
        print("Thank you! Goodbye!")
        break
    
    if code not in products:
        print("Invalid code! Please try again.")
        continue
    
    if products[code]["stock"] <= 0:
        print(" Out of stock!")
        continue
    
    name = products[code]["name"]
    price = products[code]["price"]
    
    print("\nYou selected: " + name)
    print("Price: " + str(price) + " SAR")
    
    money = float(input("Insert money (SAR): "))
    
    if money < price:
        print("Insufficient Balance! " + str(money) + " SAR")
        continue
    
    change = money - price
    products[code]["stock"] -= 1
    
    print("\n" + "-" * 40)
    print("Dispensing: " + name)
    print("Your change: " + str(change) + " SAR")
    print("-" * 40)
    # This will prompt the user and suggest an item that pairs well with the selected product
    if name in suggestions:
        suggestion = suggestions[name]
        print(f"\nWould you like to add {suggestion}? It pairs well with {name}!")
    # This will prompt the user if the user would like to buy more
    again = input("\nBuy more? (yes/no): ")
    if again != "yes":
        print("Thank you for your purchase! Goodbye!")
        break