'''
Ability to delete a 
person using 
person's name - Use Console to delete a person

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

    print("adding a new contact...")
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

    print("address Book:")
    for idx, contact in enumerate(address_book):
        print(f"Contact {idx + 1}:")
        for key, value in contact.items():
            print(f"  {key}: {value}")
        print()
    if not address_book:
        print("data is not found!!")

    print()


def edit_contact(address_book):

    search_name = input("Enter the first name of the contact to edit: ")
    search_last_name = input("Enter the last name of the contact to edit: ")

    contact_found = False
    for contact in address_book:
        if contact["First Name"].lower() == search_name.lower() and contact["Last Name"].lower() == search_last_name.lower():
            contact_found = True

            print("Contact found Enter new details (press Enter to change data):")

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

def main():

    address_book = []
    while True:
        print("Address Book Menu:")
        print("1. Add a new contact")
        print("2. Display all contacts")
        print("3. Edit an existing contact")
        print("4. delete the contact")
        print("5.exit")

        choice = input("Choose an option (1/2/3/4/5): ")

        if choice == "1":
            add_contact(address_book)
        elif choice == "2":
            display_contacts(address_book)
        elif choice == "3":
            edit_contact(address_book)
        elif choice == "4":
            delete_contact(address_book)

        elif choice=="5":
            print("exit the program")
            break
        else:
            print("Invalid choice. Please choose again.")


if __name__ == '__main__':
    main()
