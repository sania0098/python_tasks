import json


def view_books():
    with open('data/books.json', 'r') as file:
        books = json.load(file)

    available_books = []
    for book in books:
        available_copies = book['copies'] - book['borrowed']
        available_books.append({
            "title": book['title'],
            "author": book['author'],
            "available_copies": available_copies
        })

    return available_books
