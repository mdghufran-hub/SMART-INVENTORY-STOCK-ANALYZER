

from inventory import inventory




def kth_smallest():

    print("\n========== KTH SMALLEST STOCK ==========")

    if len(inventory) == 0:
        print("Inventory is empty.")
        return

    

    quantities = []

    for product in inventory:

        quantity = inventory[product]["quantity"]

        quantities.append(quantity)



    quantities.sort()

    print("\nStock quantities in sorted order:")
    print(quantities)

    try:
        k = int(
            input("\nEnter the value of k: ")
        )
    except ValueError:
        print("Please enter a valid number.")
        return

    if k < 1 or k > len(quantities):

        print("Invalid value of k.")

    else:

        result = quantities[k - 1]

        print(
            f"{k}th smallest stock quantity = {result}"
        )




def reverse_inventory():

    print("\n========== REVERSED INVENTORY ==========")

    if len(inventory) == 0:
        print("Inventory is empty.")
        return

    

    products = list(inventory.keys())

    

    products.reverse()

    print("\nProducts in reverse order:")

    for product in products:

        print("•", product)




def sort_by_stock():

    print("\n========== PRODUCTS SORTED BY STOCK ==========")

    if len(inventory) == 0:
        print("Inventory is empty.")
        return

    

    product_list = []

    for product in inventory:

        quantity = inventory[product]["quantity"]

        product_list.append(
            (product, quantity)
        )

    

    product_list.sort(
        key=lambda item: item[1]
    )

    print("\nLowest stock → Highest stock")
    print("-" * 40)

    for product, quantity in product_list:

        print(
            f"{product:<15} → {quantity} units"
        )