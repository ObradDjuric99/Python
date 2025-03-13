# virtualna biblioteka

# crud operacije , dodaj , obrisi, izlistaj sve po funkcijama

books = []

def add_book(name, book_author):
    books.append({"name":name, "author": book_author })


add_book("Hari", "autor")

def find_book_by_name(name):
    for book in books:
        if book["name"] == name:
            return book

def delete_book(name):
    found_book = find_book_by_name(name)
    if found_book is None:
        print("Nema knjige")
    else:
        books.remove(found_book)

delete_book("Hari")

print(books)
