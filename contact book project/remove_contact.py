import save_all_contact
def remove_contact(all_contact):
    if all_contact!=[]:
         
         with open("all_contact.csv","r")as file:
            content=file.read()
           
    
            c=input(f"Enter name of the contact you want to remove: ")
            for i in range(len(all_contact)-1, -1, -1):
               
                if all_contact[i].get('name') == c:
                    del all_contact[i]  
                    print(f"The contact with name {c} removed successfully\n")
                    save_all_contact.save_all_contacts(all_contact)
                    return


           
          
    else:
         print("No contact in the list\n")