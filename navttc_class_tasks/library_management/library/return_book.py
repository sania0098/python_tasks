import json


def return_book(title):
    with open('data/books.json', 'r') as file:
        books = json.load(file)

    for book in books:
        if book['title'].lower() == title.lower() and book['borrowed'] > 0:
            book['borrowed'] -= 1
            with open('data/books.json', 'w') as file:
                json.dump(books, file, indent=4)
            return f"You have returned '{title}'."

    return f"You did not borrow '{title}', so it cannot be returned."
