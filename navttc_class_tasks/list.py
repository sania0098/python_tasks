# b=[5,3,9,6,"ali"]
# print(b[-3::-1])


# list=[1,2,3,4,5]
# print("the list is",list)
# user_num=int(input("the new value is"))
# list[-1]=user_num
# print(len(list))
# print(list)
# del list[0]
# print("updated list is",list)
#############################################
# list=[]
# for i in range(5):
#
#     list.append(i+1)
# print(list)
###############################################
# list_1=[1,2,3,4,5]
# list_2=[6,7,8,9,10]
# list_1[2]=list_2[3]
# print(list_1,list_2)
# del list_2[3]
# print(list_1,list_2)



# def insert():
#     insert_empty_list = []
#     i=0
#     while i<=5:
#         insert_empty_list.insert(i,i+1)
#         i+=1
#     print(insert_empty_list)

# def append():
#     append_empty_list = []
#     i=0
#     while i<=5:
#         append_empty_list.append(i+1)
#         i+=1
#     print(append_empty_list)
#
# print("insert function ",insert())
# print("append function ",append())
# #################################


beatles=[]
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("my initial list is",list)
for i in range(2):
    num=input("enter name")
    beatles.append(num)
print("after adding new names the list be like",beatles)
del beatles[3]
del beatles[3]
print("after deleting the list is ",beatles)
beatles.insert(2,"Ringo Starr")
print(len(beatles))
print("now the newly list is",beatles)















