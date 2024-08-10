'''
Ability to add a new
Contact to Address Book

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
    for idx, contact in enumerate(address_book):
        print(f"Contact {idx + 1}:")
        for key, value in contact.items():
            print(f"  {key}: {value}")
        print()


def main():

    address_book = []

    while True:
        print("Address Book Menu:")
        print("1. Add a new contact")
        print("2. Display all contacts")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            add_contact(address_book)
        elif choice == "2":
            display_contacts(address_book)
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice Please choose again.")



if __name__ == '__main__':
    main()






