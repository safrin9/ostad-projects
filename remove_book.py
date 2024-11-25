def remove_book(all_books):
    if all_books!=[]:
         
         with open("all_books.csv","r")as file:
            content=file.read()
            print(content)

            c=input(f"Enter title of the book you want to remove: ")
            for i in range(len(all_books) - 1, -1, -1):
               
                if all_books[i].get('title') == c:
                    del all_books[i]  
                    print(f"The book {c} removed successfully\n") 
                      
                else:
                    print(f"{c} doesn't exist in the list of books\n")                
                                    
    else:
         print("No book in the list\n")