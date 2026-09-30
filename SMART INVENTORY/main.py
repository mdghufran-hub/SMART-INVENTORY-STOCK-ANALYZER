from inventory import (
    add_product,
    remove_product,
    search_product,
    update_stock,
    display_inventory
)

from analysis import (
    maximum_stock,
    minimum_stock,
    low_stock,
    unique_categories,
    statistics
)

from sorting import (
    kth_smallest,
    reverse_inventory,
    sort_by_stock
)


def main():

    print("\n")
    print("=" * 60)
    print("    WELCOME TO SMART INVENTORY ANALYZER")
    print("=" * 60)

    print(
        "A simple Python project to manage and"
    )
    print(
        "analyze stock inventory."
    )

    while True:

        print("\n")
        print("=" * 60)
        print("          MAIN MENU")
        print("=" * 60)

        print("1. Add Product")
        print("2. Remove Product")
        print("3. Search Product")
        print("4. Update Stock")
        print("5. Display Inventory")
        print("6. Find Maximum Stock")
        print("7. Find Minimum Stock")
        print("8. Find Low Stock Products")
        print("9. Find Kth Smallest Stock")
        print("10. Show Unique Categories")
        print("11. Reverse Inventory")
        print("12. Inventory Statistics")
        print("13. Sort Products by Stock")
        print("14. Exit")

        print("-" * 60)

        choice = input(
            "Enter your choice (1-14): "
        ).strip()

        if choice == "1":
            add_product()

        elif choice == "2":
            remove_product()

        elif choice == "3":
            search_product()

        elif choice == "4":
            update_stock()

        elif choice == "5":
            display_inventory()

        elif choice == "6":
            maximum_stock()

        elif choice == "7":
            minimum_stock()

        elif choice == "8":
            low_stock()

        elif choice == "9":
            kth_smallest()

        elif choice == "10":
            unique_categories()

        elif choice == "11":
            reverse_inventory()

        elif choice == "12":
            statistics()

        elif choice == "13":
            sort_by_stock()

        elif choice == "14":
            print("\nThank you for using Smart")
            print("Inventory Analyzer!")
            print("Have a great day! 👋")
            break

        else:
            print("\nHmm... that doesn't seem to")
            print("be a valid option.\n")
            print("Please choose a number")
            print("between 1 and 14.")


if __name__ == "__main__":
    main()
