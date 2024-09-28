def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == "1":
            item = input("Enter Your Item: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to the shopping list.")
            else:
                print("Item cannot be empty")
        elif choice == "2":
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed from the shopping list")
            else:
                print(f"{item} is not in the shopping list.")
        elif choice == "3":
            print("\nshopping_list:")
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")
            else:
                print("Your Shopping list is empty")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
