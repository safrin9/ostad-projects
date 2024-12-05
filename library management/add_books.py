from save_all_books import save_all_books

def add_books(all_books):
    title=input("enter book title: ")
    author=input("enter author name: ")
    isbn=int(input("Enter ISBN number: "))
    year=int(input("enter publishing year: "))
    price=int(input("Enter price: "))
    quantity=int(input("Enter quantity: "))

    book={
        "title":title,
        "author":author,
        "ISBN":isbn,
        "year":year,
        "price":price,
        "quantity":quantity
        }
    
    all_books.append(book)
    save_all_books(all_books)
    print("Books added successfully\n")
    return all_books
