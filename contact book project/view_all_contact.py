def view_all_contacts(all_contact):
    if all_contact!=[]:
        print("----contact list----\n")
        for i,contact in enumerate(all_contact,start=1):
            print(f"{i}.Name: {contact['name']}, Email: {contact['email']}, Phone number: {contact['phone']}, Address: {contact['address']}")
        print()
    else:
        print("No saved contact found in all contact\n")        