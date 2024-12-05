def save_all_books(all_books):
    with open("all_books.csv","w")as fp:
        for book in all_books:
            line=f"{all_books.index(book)+1}. {book['title']}, {book['author']}, {book['ISBN']}, {book['year']}, {book['price']}, {book['quantity']}\n"
            fp.write(line)


