# from inventory_operation.invention import addbook,removedbook
# from return_operation import *
# from borrow_operation import *
#
#
# inventory=[]
# borrowedbook=[]
# def mainfun():
#     print(" 1 for adding book")
#     print(" 2 for remove book")
#     print(" 3 for borrow book")
#     print(" 4 for return book")
#     choice=int(input("enetr your choice; "))
#     if choice==1:
#         title=input("enetr book title which you want to add")
#         addbook(inventory,title)
#     elif choice==2:
#         title=input('enter book title which you want to removed')
#         removedbook(inventory,title)
#     elif choice==3:
#         title = input('enter book title which you want to borrow')
#         removedbook(inventory, title)
#     elif choice==4:
#         title = input('enter book title which you have to return')
#         returnbook(inventory,title)
#     else:
#         print('invalid choice')







# if __name__=="__main__":
#     mainfun()


# Homework 9 - Library Management System

from inventory_operation import *
from borrow_operation import *
from return_operation import *


def main():
    inventory = ["1984", "Harry Potter - The Half-Blood Prince", "Animal Farm"]
    borrowed_books = []

    _user_in_library = True

    while _user_in_library:
        print("\n")
        print('*' * 31)
        print("Library Management System")
        print('*' * 31)
        print("1. Borrow a Book")
        print("2. Return a Book")
        print("3. Add a Book to Inventory")
        print("4. Remove a Book from Inventory")
        print("5. View Inventory")
        print("6. View Borrowed Books")
        print("7. Exit")
        print('*' * 31)

        try:
            _user_choice = int(input("\nEnter your choice (1-7): "))
            print()

            if _user_choice == 1:
                book_title = input("Enter the Book Title you want to Borrow: ")
                borrow_book(inventory, borrowed_books, book_title)

            elif _user_choice == 2:
                book_title = input("Enter the Book Title you want to Return: ")
                return_a_book(inventory, borrowed_books, book_title)

            elif _user_choice == 3:
                book_title = input("Enter the Book Title you want to Add: ")
                add_book(inventory, book_title)

            elif _user_choice == 4:
                book_title = input("Enter the Book Title you want to Remove: ")
                remove_book(inventory, book_title)

            elif _user_choice == 5:
                print("\nBooks in Inventory:")
                for book in inventory:
                    print(f"- {book}")

            elif _user_choice == 6:
                print("\nBorrowed Books:")
                for book in borrowed_books:
                    print(f"- {book}")

            elif _user_choice == 7:
                _user_in_library = False
                print("Thank you for using the Library Management System!")

            else:
                print("\nInvalid choice! Please select a Valid Option.")

        except ValueError:
            print("\nPlease enter a valid number.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()