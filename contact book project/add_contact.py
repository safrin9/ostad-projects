from save_all_contact import save_all_contacts
def add_contact(all_contact):
    
    name=input("Enter name: ")
    email=input("Enter email: ")
    number=input("Enter phone number: ")
    address=input("enter address: ")
    
          
    contact={
        "name":name,
        "email":email,
        "phone":number,
        "address":address,
        
        }
    if not name.replace(" ", "").isalpha():
        print("Invalid input! Please enter a valid name containing only letters and spaces.")
        return 

   
    if not contact["phone"].isdigit():
        print("Invalid phone number.Phone numbers should only contain digits.")
        return
    
    for i in range(len(all_contact)-1, -1, -1):
                
                if str(all_contact[i].get('phone')) == str(contact["phone"]):       
                    print(f"Phone number already assigned to '{all_contact[i].get('name')}'.Cannot duplicate.\n") 
                    return
    
   
    all_contact.append(contact)
    save_all_contacts(all_contact)
    print("contact added successfully\n")
    return all_contact