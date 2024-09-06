# books=[]
# def addbook(inventory,booktitle):
#
#     if inventory and booktitle=='':
#         print('')
#
#     else:
#         books=[]
#         books.append(inventory)
#         books.append(booktitle)
#         print('books are added successfuly')
#
#
# def removedbook(inventory,booktitle):
#     if inventory and booktitle=='':
#         print()
#     else:
#         books.remove(inventory)
#         books.remove(booktitle)
#         print('removed book from list')

""" * This Module is for Managing Books Inventory * """


def add_book(inventory, book_title):
    if book_title not in inventory:
        inventory.append(book_title)
        print(f"\n'{book_title}' has been added to the inventory.")
    else:
        print(f"\n'{book_title}' already exists in the inventory.")


def remove_book(inventory, book_title):
    if book_title in inventory:
        inventory.remove(book_title)
        print(f"\n'{book_title}' has been removed from the inventory.")
    else:
        print(f"\n'{book_title}' does not exist in the inventory.")







