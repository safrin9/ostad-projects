import add_books
import view_all_books
import update_books
import remove_book


all_books=[]

while True:
    print("Welcome to library Management System")
    print("0. Exit")
    print("1. Add Books")
    print("2. View all Books")
    print("3. Update books")
    print("4. Remove book")
    menu=int(input("Select any number: "))
    if menu==0:
        print("Thanks for library management system")
        break
    elif menu==1:
        add_books.add_books(all_books)
    elif menu==2:
        view_all_books.view_all_books(all_books)
    elif menu==3:
        update_books.update_all_books(all_books)
    elif menu==4:
        remove_book.remove_book(all_books) 
    else:
        print("Choose a valid number")