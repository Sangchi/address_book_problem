'''
Ability to create a Contacts in Address 
Book with first and last names, address, 
city, state, zip, phone number and 
email…Ability to create a Contacts in Address 
Book with first and last names, address, 
city, state, zip, phone number and 
email…

'''

def create_contact(first_name,last_name,address,city,state,zip_code,phone_number,email):

    new_contact = {
        "First Name": first_name,
        "Last Name": last_name,
        "Address": address,
        "City": city,
        "State": state,
        "Zip Code": zip_code,
        "Phone_Number": phone_number,
        "Email": email
    }

    return new_contact


def main():

    first_name=input("enter your first name:")
    last_name=input("enter your last name:")
    address=input("enter your address:")
    city=input("enter you city:")
    state=input("enter you state:")
    zip_code=int(input("enter your zip_code:"))
    phone_number=int(input("enter your phone number:"))
    gmail=input("enter your gmail:")
    print(create_contact(first_name,last_name,address,city,state,zip_code,phone_number,gmail))


if __name__=='__main__':
    main()



'''
output-

{'First Name': 'prashant',
'Last Name': 'chavan',
 'Address': 'vaishnvai avenue a wing nahre', 
 'City': 'pune',
 'State': 'maharastra411041', 
 'Zip Code': 411041, 
 'Phone_Number': 9921793120,
 'Email': 'prashantchavan@gmail.com'}


'''




