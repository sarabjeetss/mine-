phoneDirectory = {}  # Create an empty dictionary to store phone directory

# Display the main menu to the user
print("WELCOME TO THE GRANN'S PHONE DIRECTORY")
r=0


while True:
    if(r==1):
        print("\nMenu\n")
        
        
    print("1. Add a record")
    print("2. Search a record")
    print("3. Change a record")
    print("4. Delete a record")
    print("5. Quit")

    r=1
    # Loop through the menu until the user chooses to quit
    choice = input("\nEnter your choice: ")

    if choice == '1':
        # If the user chooses to add a record, get the name and phone number from the user and add them to the dictionary
        name = input("\nEnter name: ")
        phone = input("Enter your 10-digit phone number: ")
        if phone.isdigit() and len(phone) == 10:
            phoneDirectory[name] = phone
            print("Record added")
        else:
            print("Invalid phone number. Please enter a 10-digit phone number.")

    elif choice == '2':
        # If the user chooses to search for a record, get the name from the user and search the dictionary for the corresponding phone number
        name = input("\nEnter name to search: ")
        if name in phoneDirectory:
            print(name + ": " + phoneDirectory[name])
        else:
            print("Record not found")

    elif choice == '3':
        # If the user chooses to update a record, get the name and new phone number from the user and update the corresponding entry in the dictionary
        name = input("\nEnter name: ")
        if name in phoneDirectory:
            phone = input("Enter new 10-digit phone number: ")
            if phone.isdigit() and len(phone) == 10:
                phoneDirectory[name] = phone
                print("Record updated")
            else:
                print("Invalid phone number. Please enter a 10-digit phone number.")
        else:
            print("Record not found")

    elif choice == '4':
        # If the user chooses to delete a record, get the name from the user and delete the corresponding entry from the dictionary
        name = input("\nEnter name: ")
        if name in phoneDirectory:
            del phoneDirectory[name]
            print("Record deleted")
        else:
            print("Record not found")

    elif choice == '5':
        # If the user chooses to quit, break out of the loop
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.\n")
