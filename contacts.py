def contacts():
    
    print("Contacts")

    def contact_menu():
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Delete Contacts")
        print("4. Back to Main Menu")

        choice = int(input("Please choose an option (1-4): "))
        return choice

    choice = contact_menu()

    if choice == 1:
        phone_number = input("Please enter their phone number: ")
        name = input("Please enter their name: ")
        address = input("Please enter their address: ")

    elif choice == 2:
        pass

    elif choice == 3:
        pass

    elif choice == 4:
        print("Ok,returning to main menu")

    else:
        print("Choice is invalid, please choose again")