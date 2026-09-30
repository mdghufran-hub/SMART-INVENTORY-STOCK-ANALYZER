

from inventory import inventory




def maximum_stock():

    print("\n========== MAXIMUM STOCK ==========")

    if len(inventory) == 0:
        print("Inventory is empty.")
        return

    maximum = -1
    product_name = ""

    for product in inventory:

        quantity = inventory[product]["quantity"]

        if quantity > maximum:

            maximum = quantity
            product_name = product

    print(
        f"Product with highest stock: {product_name}"
    )

    print(
        f"Available quantity: {maximum}"
    )




def minimum_stock():

    print("\n========== MINIMUM STOCK ==========")

    if len(inventory) == 0:
        print("Inventory is empty.")
        return

    minimum = None
    product_name = ""

    for product in inventory:

        quantity = inventory[product]["quantity"]

        if minimum is None or quantity < minimum:

            minimum = quantity
            product_name = product

    print(
        f"Product with lowest stock: {product_name}"
    )

    print(
        f"Available quantity: {minimum}"
    )




def low_stock():

    print("\n========== LOW STOCK ANALYZER ==========")

    if len(inventory) == 0:
        print("Inventory is empty.")
        return

    try:
        limit = int(
            input("Enter low-stock limit: ")
        )
    except ValueError:
        print("Please enter a valid number.")
        return

    found = False

    print("\nProducts below the selected limit:")
    print("-" * 40)

    for product in inventory:

        quantity = inventory[product]["quantity"]

        if quantity < limit:

            print(
                f"{product:<15} → {quantity} units"
            )

            found = True

    if found == False:

        print("Good news! No products are running low.")




def unique_categories():

    print("\n========== UNIQUE CATEGORIES ==========")

    if len(inventory) == 0:
        print("Inventory is empty.")
        return

    categories = set()

    for product in inventory:

        category = inventory[product]["category"]

        categories.add(category)

    print("Available categories:")

    for category in categories:

        print("•", category)



def statistics():

    print("\n========== INVENTORY STATISTICS ==========")

    if len(inventory) == 0:
        print("Inventory is empty.")
        return

    total_products = len(inventory)

    total_stock = 0

    total_value = 0

    for product in inventory:

        quantity = inventory[product]["quantity"]

        price = inventory[product]["price"]

        total_stock = total_stock + quantity

        total_value = total_value + (
            quantity * price
        )

    average_stock = total_stock / total_products

    print("Number of different products :", total_products)

    print("Total number of items        :", total_stock)

    print(
        "Total inventory value        : ₹",
        total_value
    )

    print(
        "Average stock per product   :",
        round(average_stock, 2)
    )