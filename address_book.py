'''
Refactor to add multiple
Address Book to the
System. Each Address Book
has a unique Name

'''

def create_contact(first_name, last_name, address, city, state, zip_code, phone_number, email):

    return {
        "First Name": first_name,
        "Last Name": last_name,
        "Address": address,
        "City": city,
        "State": state,
        "Zip Code": zip_code,
        "Phone Number": phone_number,
        "Email": email
    }

def add_contact(address_book):

    print("Adding a new contact...")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    address = input("Enter address: ")
    city = input("Enter city: ")
    state = input("Enter state: ")
    zip_code = input("Enter zip code: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    
    contact = create_contact(first_name, last_name, address, city, state, zip_code, phone_number, email)
    address_book.append(contact)
    print("Contact added successfully!")

def display_contacts(address_book):

    print("Address Book:")
    if not address_book:
        print("No contacts found!")
        return
    
    for idx, contact in enumerate(address_book):
        print(f"Contact {idx + 1}:")
        for key, value in contact.items():
            print(f"  {key}: {value}")
        print()

def edit_contact(address_book):

    search_name = input("Enter the first name of the contact to edit: ")
    search_last_name = input("Enter the last name of the contact to edit: ")
    
    contact_found = False
    for contact in address_book:
        if contact["First Name"].lower() == search_name.lower() and contact["Last Name"].lower() == search_last_name.lower():
            contact_found = True

            print("Contact found. Enter new details (press Enter to keep existing data):")
            
            contact["First Name"] = input(f"Enter new first name (current: {contact['First Name']}): ") or contact["First Name"]
            contact["Last Name"] = input(f"Enter new last name (current: {contact['Last Name']}): ") or contact["Last Name"]
            contact["Address"] = input(f"Enter new address (current: {contact['Address']}): ") or contact["Address"]
            contact["City"] = input(f"Enter new city (current: {contact['City']}): ") or contact["City"]
            contact["State"] = input(f"Enter new state (current: {contact['State']}): ") or contact["State"]
            contact["Zip Code"] = input(f"Enter new zip code (current: {contact['Zip Code']}): ") or contact["Zip Code"]
            contact["Phone Number"] = input(f"Enter new phone number (current: {contact['Phone Number']}): ") or contact["Phone Number"]
            contact["Email"] = input(f"Enter new email (current: {contact['Email']}): ") or contact["Email"]
            
            print("Contact updated successfully!")
            break
    
    if not contact_found:
        print("Contact not found.")


def delete_contact(address_book):

    search_name = input("Enter the first name of the contact to delete: ")
    search_last_name = input("Enter the last name of the contact to delete: ")
    
    contact_found = False
    for contact in address_book:
        if contact["First Name"].lower() == search_name.lower() and contact["Last Name"].lower() == search_last_name.lower():
            address_book.remove(contact)
            contact_found = True
            print("Contact deleted successfully!")
            break
    
    if not contact_found:
        print("Contact not found.")

def add_multiple_contacts(address_book):

    data_add_count = int(input("Enter the number of contacts you want to add: "))
    for i in range(data_add_count):
        print(f"Adding contact {i + 1}...")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        address = input("Enter address: ")
        city = input("Enter city: ")
        state = input("Enter state: ")
        zip_code = input("Enter zip code: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        
        
    contact = create_contact(first_name, last_name, address, city, state, zip_code, phone_number, email)
    address_book.append(contact)
    print("Contact added successfully!")


def add_address_book(address_books):

    name = input("Enter the name for the new address book: ")
    if name in address_books:
        print("An address book with this name already exists.")
    else:
        address_books[name] = []
        print(f"Address book '{name}' created successfully!")

def switch_address_book(address_books):

    print("Available address books:")
    for name in address_books:
        print(f"- {name}")
    
    name = input("Enter the name of the address book to switch to: ")
    if name in address_books:
        return address_books[name]
    else:
        print("Address book not found.")
        return None

def main():

    address_books = {}
    current_address_book = None

    while True:
        print("Address Book System Menu:")
        print("1. Add a new address book")
        print("2. Switch address book")
        print("3. Add a new contact")
        print("4. Display all contacts")
        print("5. Edit an existing contact")
        print("6. Delete a contact")
        print("7. Add multiple contacts")
        print("8. Exit")
        
        choice = input("Choose an option (1/2/3/4/5/6/7/8): ")
        
        if choice == "1":
            add_address_book(address_books)
        elif choice == "2":
            current_address_book = switch_address_book(address_books)
        elif choice == "3":
            if current_address_book is None:
                print("No address book selected. Please switch to an address book first.")
            else:
                add_contact(current_address_book)
        elif choice == "4":
            if current_address_book is None:
                print("No address book selected. Please switch to an address book first.")
            else:
                display_contacts(current_address_book)
        elif choice == "5":
            if current_address_book is None:
                print("No address book selected. Please switch to an address book first.")
            else:
                edit_contact(current_address_book)
        elif choice == "6":
            if current_address_book is None:
                print("No address book selected. Please switch to an address book first.")
            else:
                delete_contact(current_address_book)
        elif choice == "7":
            if current_address_book is None:
                print("No address book selected. Please switch to an address book first.")
            else:
                add_multiple_contacts(current_address_book)
        elif choice == "8":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice!")


if __name__ == '__main__':
    main()
