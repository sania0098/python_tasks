from inventory_operation.invention import addbook,removedbook
from return_operation import *
from borrow_operation import *


inventory=[]
borrowedbook=[]
def mainfun():
    print(" 1 for adding book")
    print(" 2 for remove book")
    print(" 3 for borrow book")
    print(" 4 for return book")
    choice=int(input("enetr your choice; "))
    if choice==1:
        title=input("enetr book title which you want to add")
        addbook(inventory,title)
    elif choice==2:
        title=input('enter book title which you want to removed')
        removedbook(inventory,title)
    elif choice==3:
        title = input('enter book title which you want to borrow')
        removedbook(inventory, title)
    elif choice==4:
        title = input('enter book title which you have to return')
        returnbook(inventory,title)
    else:
        print('invalid choice')







if __name__=="__main__":
    mainfun()