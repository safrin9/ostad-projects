import csv

def load_contacts():
    contacts = []
    try:
        with open("all_contact.csv", "r") as file:
            reader= csv.DictReader(file)  
            for row in reader:
                contacts.append(row)
   
    except Exception as e:
        print(f"Error loading contacts: {e}")
    return contacts