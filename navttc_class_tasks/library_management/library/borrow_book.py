import json


def borrow_book(title):
    with open('data/books.json', 'r') as file:
        books = json.load(file)

    for book in books:
        if book['title'].lower() == title.lower() and book['copies'] > book['borrowed']:
            book['borrowed'] += 1
            with open('data/books.json', 'w') as file:
                json.dump(books, file, indent=4)
            return f"You have borrowed '{title}'."

    return f"'{title}' is not available right now."
