# user_input = input("enter any word")
# user_input = user_input.upper()
# vowel_word = "AEIOU"
# remaining_word=""
#
# for letter in user_input:
#     if letter in vowel_word:
#         continue
#
#     remaining_word+=letter
#
# print( remaining_word)
#


#####################################################################################
# blocks = int(input("Enter the number of blocks: "))
# layer = 1
# usedblock = 0
# while blocks >= usedblock + layer:
#     usedblock = usedblock + layer
#     layer += 1
#
# print("The height of the pyramid:", layer - 1)
############################################################################

# c0=int(input("enetr any number"))
# steps=1
# while c0>0:
#     if c0%2==0:
#         c0=c0%2
#
#
#         print(c0)
#     elif c0%2!=0:
#         c0=3*c0+1
#
#         print(c0)
#     else:
#         c0 = 3 * c0 + 1
#         print(c0)
# steps+=steps
# print(steps)
# 33333333################################################################################################
# lst = [1, 2, 3, 4, 5,7,8,8,9,9,9,9,9]  # Example list
# middle_index = len(lst) // 2
# lst[middle_index] = int(input("Enter a number to replace the middle element: "))
# lst.pop()
# print(len(lst))
# print(lst)len


# x=2
# y=4
# x=x // y
# y=y // x
# y=2 + 3 * 5
# print(1 // 2*3)

# mylist=[1,2,3]
# for v in range(len(mylist)):
#     mylist.insert(1,mylist[v])
# print(mylist)
# mylist=[[0,1,2,3] for i in range (2)]
# print(mylist[2][0])
# var=1
# while var<10:
#     print("#")
#     var=var<<1
# list1=[1,2,3]
#
# list=[0,1,2]
# list.insert(0,1)
# del list[1]
# print(list)
def fun():
    global x
    x=4
    print("hello",x)
x=3
fun()
print(x)
def fun2() :
    global x
    x=6
    print("hello",x)
x=3
fun2()
print(x)
