import json   #used  to store and transfer structured data.
import os           #The os.path.exists() function helps avoid this by allowing you to check if the file exists before attempting to read it.


def add_book(title, author, copies):
    new_book = {
        "title": title,
        "author": author,
        "copies": copies,
        "borrowed": 0
    }
    #Even if a file exists, it might be empty.
    # Attempting to load an empty file with json.load() would cause an error.
    # The os.path.getsize() function returns the size of the file in bytes,
    # and if it's 0, the file is empty.
    # Check if the file exists and is not empty
    if os.path.exists('data/books.json') and os.path.getsize('data/books.json') > 0:
        with open('data/books.json', 'r') as file:
            try:
                books = json.load(file)
            except json.JSONDecodeError:
                books = []
    else:
        books = []

    books.append(new_book)

    with open('data/books.json', 'w') as file:
        json.dump(books, file, indent=4)

    print(f"Book '{title}' by {author} added successfully!")
