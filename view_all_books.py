def view_all_books(all_books):
    if all_books!=[]:
        for book in all_books:
            print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['ISBN']}, Year: {book['year']}, Price: {book['price']}, Quantity: {book['quantity']}\n")

    else:
        print("No book found in all books\n")        