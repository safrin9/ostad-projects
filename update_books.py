
def update_all_books(all_books):
    
    def update(a,name):
        c=input(f"enter new {name}: ")
                
        all_books[a][name]=c
        print(f"{name} updated successfully\n")   

    with open("all_books.csv","r") as file:
        content=file.read()
        print(content)
        
        
        
        if all_books!=[]:
            a=int(input("which book do you want to update? (please enter valid book number) "))
            a=a-1

            
            print("1. update book title")
            print("2. update author")
            print("3. update isbn")
            print("4. update publishing year")
            print("5. update price")
            print("6. update quantity")
        
            m=int(input("enter any number you want to update: "))
        
            if m==1:
                update(a,'title')
            if m==2:
                update(a,'author')
            if m==3:
                update(a,'ISBN')    
            if m==4:
                update(a,'year')
            if m==5:
                update(a,'price')
            if m==6:
                update(a,'quantity')

           
           
        else:
            print("No books to update. Add books first.\n")

       