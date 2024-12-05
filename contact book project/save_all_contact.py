import csv
def save_all_contacts(all_contact):
    with open("all_contact.csv","w")as file:

        fieldnames = ['name',"email","phone","address"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(all_contact)
    
    





        # for contact in all_contact:
        #     line=f"{contact['name']}, {contact['email']}, {contact['phone']}, {contact['address']}\n"
        #     file.write(line)
        
