'''
Ability to Read/Write
the Address Book
with Persons Contact
as CSV File

'''
import csv


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

    print("adding a new contact...")
    first_name = input("enter first name: ")
    last_name = input("enter last name: ")
    address = input("enter address: ")
    city = input("enter city: ")
    state = input("enter state: ")
    zip_code = input("enter zip code: ")
    phone_number = input("enter phone number: ")
    email = input("enter email: ")

    contact = create_contact(first_name, last_name, address, city, state, zip_code, phone_number, email)
    address_book.append(contact)
    print("contact added successfully!")

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
        print("no contacts found!")
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
        print("invalid choice. displaying contacts without sorting.")

    print("address Book:")
    for idx, contact in enumerate(address_book):
        print(f"contact {idx + 1}:")
        for key, value in contact.items():
            print(f"  {key}: {value}")
        print()


def edit_contact(address_book):

    search_name = input("enter the first name of the contact to edit: ")
    search_last_name = input("enter the last name of the contact to edit: ")

    contact_found = False
    for contact in address_book:
        if contact["First Name"].lower() == search_name.lower() and contact["Last Name"].lower() == search_last_name.lower():
            contact_found = True

            print("contact found. enter new details (press Enter to keep existing data):")

            contact["First Name"] = input(f"enter new first name (current: {contact['First Name']}): ") or contact["First Name"]
            contact["Last Name"] = input(f"enter new last name (current: {contact['Last Name']}): ") or contact["Last Name"]
            contact["Address"] = input(f"enter new address (current: {contact['Address']}): ") or contact["Address"]
            contact["City"] = input(f"enter new city (current: {contact['City']}): ") or contact["City"]
            contact["State"] = input(f"enter new state (current: {contact['State']}): ") or contact["State"]
            contact["Zip Code"] = input(f"enter new zip code (current: {contact['Zip Code']}): ") or contact["Zip Code"]
            contact["Phone Number"] = input(f"enter new phone number (current: {contact['Phone Number']}): ") or contact["Phone Number"]
            contact["Email"] = input(f"enter new email (current: {contact['Email']}): ") or contact["Email"]

            print("contact updated successfully!")
            break

    if not contact_found:
        print("contact not found.")


def delete_contact(address_book):

    search_name = input("enter the first name of the contact to delete: ")
    search_last_name = input("enter the last name of the contact to delete: ")

    contact_found = False
    for contact in address_book:
        if contact["First Name"].lower() == search_name.lower() and contact["Last Name"].lower() == search_last_name.lower():
            address_book.remove(contact)
            contact_found = True
            print("contact deleted successfully!")
            break

    if not contact_found:
        print("contact not found.")


def add_multiple_contacts(address_book):

    data_add_count = int(input("enter the number of contacts you want to add: "))
    for i in range(data_add_count):
        print(f"adding contact {i + 1}...")
        first_name = input("enter first name: ")
        last_name = input("enter last name: ")
        address = input("enter address: ")
        city = input("enter city: ")
        state = input("enter state: ")
        zip_code = input("enter zip code: ")
        phone_number = input("enter phone number: ")
        email = input("enter email: ")

        if any(contact["First Name"].lower() == first_name.lower() and contact["Last Name"].lower() == last_name.lower() for contact in address_book):
            print("the contact is already in the address book. Cannot add duplicate data!")
        else:
            contact = create_contact(first_name, last_name, address, city, state, zip_code, phone_number, email)
            address_book.append(contact)
            print("contact added successfully!")


def add_address_book(address_books):

    name = input("enter the name for the new address book: ")
    if name in address_books:
        print("an address book with this name already exists.")
    else:
        address_books[name] = []
        print(f"address book '{name}' created successfully!")


def switch_address_book(address_books):

    print("available address books:")
    for name in address_books:
        print(f"- {name}")

    name = input("enter the name of the address book to switch to: ")
    if name in address_books:
        return address_books[name]
    else:
        print("address book not found.")
        return None


def search_or_count_person(address_book):

    print("search or Count by:")
    print("1. Search by City")
    print("2. Search by State")
    print("3. Count by City")
    print("4. Count by State")

    search_choice = input("Choose an option (1/2/3/4): ")

    if search_choice == "1":
        search_city = input("enter the city to search: ").lower()
        found_contacts = [contact for contact in address_book if search_city in contact["City"].lower()]
        if found_contacts:
            print("found contact(s):")
            for contact in found_contacts:
                print(f"  {contact}")
        else:
            print("no contacts found.")

    elif search_choice == "2":
        search_state = input("enter the state to search: ").lower()
        found_contacts = [contact for contact in address_book if search_state in contact["State"].lower()]
        if found_contacts:
            print("found contact(s):")
            for contact in found_contacts:
                print(f"  {contact}")
        else:
            print("no contacts found.")

    elif search_choice == "3":
        count_city = input("enter the city to count: ").lower()
        count = sum(1 for contact in address_book
                    if count_city in contact["City"].lower())
        print(f"number of contacts in '{count_city}': {count}")

    elif search_choice == "4":
        count_state = input("enter the state to count: ").lower()
        count = sum(1 for contact in address_book
                    if count_state in contact["State"].lower())
        print(f"number of contacts in '{count_state}': {count}")

    else:
        print("invalid option.")


def save_address_book_to_csv(address_books, filename):

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for book_name, contacts in address_books.items():
            writer.writerow([f"Book:{book_name}"])  
            for contact in contacts:
                writer.writerow([contact['First Name'], contact['Last Name'], contact['Address'], contact['City'], contact['State'], contact['Zip Code'], contact['Phone Number'], contact['Email']])
    print(f"address book saved to '{filename}'.")

def load_address_book_from_csv(filename):

    address_books = {}
    current_book_name = None
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0].startswith("Book:"):
                    current_book_name = row[0][len("Book:"):].strip()
                    address_books[current_book_name] = []
                elif current_book_name and row:
                    if len(row) == 8:
                        contact = create_contact(*row)
                        address_books[current_book_name].append(contact)
    except FileNotFoundError:
        print("File not found. Starting with an empty address book.")
    return address_books


def main():

    address_books = {}
    current_address_book = None

    while True:
        print("address Book System Menu:")
        print("1. add a new address book")
        print("2. switch address book")
        print("3. add a new contact")
        print("4. display all contacts")
        print("5. edit an existing contact")
        print("6. delete a contact")
        print("7. add multiple contacts")
        print("8. search or Count contacts")
        print("9. save address book to CSV file")
        print("10. load address book from CSV file")
        print("11. exit")

        choice = input("choose an option (1/2/3/4/5/6/7/8/9/10/11): ")

        if choice == "1":
            add_address_book(address_books)
        elif choice == "2":
            current_address_book = switch_address_book(address_books)
        elif choice == "3":
            if current_address_book is None:
                print("no address book selected. Please switch to an address book first.")
            else:
                add_contact(current_address_book)
        elif choice == "4":
            if current_address_book is None:
                print("no address book selected. Please switch to an address book first.")
            else:
                display_contacts(current_address_book)
        elif choice == "5":
            if current_address_book is None:
                print("no address book selected. Please switch to an address book first.")
            else:
                edit_contact(current_address_book)
        elif choice == "6":
            if current_address_book is None:
                print("no address book selected. Please switch to an address book first.")
            else:
                delete_contact(current_address_book)
        elif choice == "7":
            if current_address_book is None:
                print("no address book selected. Please switch to an address book first.")
            else:
                add_multiple_contacts(current_address_book)
        elif choice == "8":
            if current_address_book is None:
                print("no address book selected. Please switch to an address book first.")
            else:
                search_or_count_person(current_address_book)
        elif choice == "9":
            filename = input("enter the filename to save: ")
            save_address_book_to_csv(address_books, filename)
        elif choice == "10":
            filename = input("enter the filename to load: ")
            address_books = load_address_book_from_csv(filename)
            print("address book loaded successfully.")
        elif choice == "11":
            print("exiting the program.")
            break
        else:
            print("invalid choice!")


if __name__ == '__main__':
    main()
