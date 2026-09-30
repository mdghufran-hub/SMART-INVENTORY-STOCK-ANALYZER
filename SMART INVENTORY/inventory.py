inventory = {

"Laptop": {

"quantity": 50,

"price": 155000,

"category": "Electronics"

},

"Mouse": {

"quantity": 100,

"price": 900,

"category": "Electronics"

},

"Keyboard": {

"quantity": 100,

"price": 1200,

"category": "Electronics"

},

"Notebook": {

"quantity": 500,

"price": 100,

"category": "Stationery"

},

"Pen": {

"quantity": 1200,

"price": 20,

"category": "Stationery"

}

}

def add_product():
	name = input("Enter product name: ").strip()
	if not name:
		print("Product name cannot be empty.")
		return
	if name in inventory:
		print("That product already exists.")
		return

	try:
		quantity = int(input("Enter quantity: "))
		price = float(input("Enter price: "))
	except ValueError:
		print("Quantity and price must be valid numbers.")
		return

	if quantity < 0 or price < 0:
		print("Quantity and price cannot be negative.")
		return

	category = input("Enter category: ").strip()
	inventory[name] = {
		"quantity": quantity,
		"price": price,
		"category": category,
	}
	print(f"{name} added to inventory.")


def remove_product():
	name = input("Enter product name to remove: ").strip()
	if name not in inventory:
		print("Product not found.")
		return

	del inventory[name]
	print(f"{name} removed from inventory.")


def search_product():
	name = input("Enter product name to search: ").strip()
	product = inventory.get(name)
	if product is None:
		print("Product not found.")
		return

	print(f"Name: {name}")
	print(f"Quantity: {product['quantity']}")
	print(f"Price: {product['price']}")
	print(f"Category: {product['category']}")


def update_stock():
	name = input("Enter product name to update: ").strip()
	if name not in inventory:
		print("Product not found.")
		return

	try:
		quantity = int(input("Enter new quantity: "))
	except ValueError:
		print("Quantity must be a valid whole number.")
		return

	if quantity < 0:
		print("Quantity cannot be negative.")
		return

	inventory[name]["quantity"] = quantity
	print(f"Stock for {name} updated to {quantity}.")


def display_inventory():
	print("\n========== CURRENT INVENTORY ==========")
	if not inventory:
		print("Inventory is empty.")
		return

	for name, product in inventory.items():
		print(
			f"{name}: quantity={product['quantity']}, "
			f"price={product['price']}, category={product['category']}"
		)
