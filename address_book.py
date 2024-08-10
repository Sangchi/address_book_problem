'''
Ability to Read or
Write the Address
Book with Persons
Contact as JSON File

'''
import json


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


def sort_contacts_by_name(address_book):

    address_book.sort(key=lambda x: (x["First Name"].lower(), x["Last Name"].lower()))

def sort_contacts_by_city(address_book):

    address_book.sort(key=lambda x: x["City"].lower())

def sort_contacts_by_state(address_book):

    address_book.sort(key=lambda x: x["State"].lower())

def sort_contacts_by_zip(address_book):

    address_book.sort(key=lambda x: x["Zip Code"].lower())

def display_contacts(address_book):

    if not address_book:
        print("No contacts found!")
        return

    sort_choice = input("Sort by (1) Name, (2) City, (3) State, (4) Zip Code: ")

    if sort_choice == "1":
        sort_contacts_by_name(address_book)
    elif sort_choice == "2":
        sort_contacts_by_city(address_book)
    elif sort_choice == "3":
        sort_contacts_by_state(address_book)
    elif sort_choice == "4":
        sort_contacts_by_zip(address_book)
    else:
        print("Invalid choice. Displaying contacts without sorting.")

    print("Address Book:")
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

        if any(contact["First Name"].lower() == first_name.lower() and contact["Last Name"].lower() == last_name.lower() for contact in address_book):
            print("The contact is already in the address book. Cannot add duplicate data!")
        else:
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

def search_or_count_person(address_book):

    print("Search or Count by:")
    print("1. Search by City")
    print("2. Search by State")
    print("3. Count by City")
    print("4. Count by State")

    search_choice = input("Choose an option (1/2/3/4): ")

    if search_choice == "1":
        search_city = input("Enter the city to search: ").lower()
        found_contacts = [contact for contact in address_book if search_city in contact["City"].lower()]
        if found_contacts:
            print("Found contact(s):")
            for contact in found_contacts:
                print(f"  {contact}")
        else:
            print("No contacts found.")

    elif search_choice == "2":
        search_state = input("Enter the state to search: ").lower()
        found_contacts = [contact for contact in address_book if search_state in contact["State"].lower()]
        if found_contacts:
            print("Found contact(s):")
            for contact in found_contacts:
                print(f"  {contact}")
        else:
            print("No contacts found.")

    elif search_choice == "3":
        count_city = input("Enter the city to count: ").lower()
        count = sum(1 for contact in address_book
                    if count_city in contact["City"].lower())
        print(f"Number of contacts in '{count_city}': {count}")

    elif search_choice == "4":
        count_state = input("Enter the state to count: ").lower()
        count = sum(1 for contact in address_book
                    if count_state in contact["State"].lower())
        print(f"Number of contacts in '{count_state}': {count}")

    else:
        print("Invalid option.")

def save_address_book_to_file(address_books, filename):

    with open(filename, 'w') as file:
        json.dump(address_books, file, indent=4)
    print(f"Address book saved to '{filename}'.")

def load_address_book_from_file(filename):

    try:
        with open(filename, 'r') as file:
            address_books = json.load(file)
        print(f"Address book loaded from '{filename}'.")
        return address_books
    except FileNotFoundError:
        print(f"No file named '{filename}' found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error decoding the file '{filename}'.")
        return {}


def main():

    address_books = {}
    current_address_book = None

    while True:
        print("\nAddress Book System Menu:")
        print("1. Add a new address book")
        print("2. Switch address book")
        print("3. Add a new contact")
        print("4. Display all contacts")
        print("5. Edit an existing contact")
        print("6. Delete a contact")
        print("7. Add multiple contacts")
        print("8. Search or Count contacts")
        print("9. Save address book to file")
        print("10. Load address book from file")
        print("11. Exit")

        choice = input("Choose an option (1/2/3/4/5/6/7/8/9/10/11): ")

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
            if current_address_book is None:
                print("No address book selected. Please switch to an address book first.")
            else:
                search_or_count_person(current_address_book)
        elif choice == "9":
            filename = input("Enter filename to save address book: ")
            save_address_book_to_file(address_books, filename)
        elif choice == "10":
            filename = input("Enter filename to load address book: ")
            address_books = load_address_book_from_file(filename)
            if address_books:
                current_address_book = next(iter(address_books.values()), None)
        elif choice == "11":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice!")


if __name__ == '__main__':
    main()
