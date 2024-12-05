import csv

def search(all_contact): 
    c = input(f"name of the contact you want to search: ").strip()
    
    with open("all_contact.csv", "r") as file:
        reader = csv.DictReader(file)
        contact_found=False 
        for row in reader:
            
            if row['name'].strip().lower()== c.lower():
                    contact_found = True
                    print(f"Name: {row['name']}, Email: {row['email']}, Phone: {row['phone']}, Phone: {row['address']}\n")
                    break
        
        if not contact_found:
            print(f"Contact with name '{c}' not found.")