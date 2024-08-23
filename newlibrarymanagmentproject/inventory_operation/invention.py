books=[]
def addbook(inventory,booktitle):

    if inventory and booktitle=='':
        print('')

    else:
        books=[]
        books.append(inventory)
        books.append(booktitle)
        print('books are added successfuly')


def removedbook(inventory,booktitle):
    if inventory and booktitle=='':
        print()
    else:
        books.remove(inventory)
        books.remove(booktitle)
        print('removed book from list')









