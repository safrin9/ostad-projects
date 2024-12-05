import add_contact
import view_all_contact
import load
import remove_contact
import search_contact

# all_contact=[]

all_contact = load.load_contacts()


while True:
    print("Welcome to Contact Book Management System")
    print("0. Exit")
    print("1. Add Contact")
    print("2. View all contacts")
    print("3. Remove contact")
    print("4. Search contact")

    menu=int(input("Select any number: "))
    if menu==0:
        print("Thanks for using Contact Book Management System")
        break
    elif menu==1:
        add_contact.add_contact(all_contact)
    elif menu==2:
        view_all_contact.view_all_contacts(all_contact)
    
    elif menu==3:
        remove_contact.remove_contact(all_contact)
    elif menu==4:
        search_contact.search(all_contact)
    else:
        print("Choose a valid number")