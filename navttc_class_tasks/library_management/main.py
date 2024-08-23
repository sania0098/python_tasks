from library.add_book import add_book
from library.borrow_book import borrow_book
from library.return_book import return_book
from library.view_books import view_books


def main():
    print("Welcome to the Library Management System!")

    while True:
        print("\nOptions:")
        print("1. Add a Book")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. View Available Books")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            copies = int(input("Enter number of copies: "))
            add_book(title, author, copies)
            print(f"'{title}' by {author} added successfully!")

        elif choice == '2':
            title = input("Enter the title of the book to borrow: ")
            message = borrow_book(title)
            print(message)

        elif choice == '3':
            title = input("Enter the title of the book to return: ")
            message = return_book(title)
            print(message)

        elif choice == '4':
            books = view_books()
            print("\nAvailable Books:")
            for book in books:
                print(f"{book['title']} by {book['author']} - {book['available_copies']} copies available")

        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
