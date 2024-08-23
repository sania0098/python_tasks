# squares = [x ** 2 for x in range(10)]
# odds = [x for x in squares if x % 2 != 0 ]
# print("squares", squares)
# print("odds in squares", odds)
###########################################

# board = []
# EMPTY = "E"
# laptop = "l"
# world = "w"
# for i in range(8):
#     row = [EMPTY for i in range(8)]
#     board.append(row)
#
# board.append(row)
# board[0][4] = laptop
# board[0][3] = world
#
# for row in board:
#     for item in row:
#         print(item, end=" ")
#     print()
##########################################
# import random
#
# temps = [[0.0 for h in range(24)] for d in range(31)]
# for i in range(31):
#     for j in range(24):
#         temps[i][j] = random.uniform(-10.0, 35.0)
# total = 0.0
# for day in temps:
#     total += day[11]
# average = total / 31
# print("the average is", average)
# highest_tem = -100.0
# for day in temps:
#     for temps in day:
#         if temps > highest_tem:
#             highest_tem = temps

# print("the highest value is", highest_tem)
###################################3
# import random

# temps = [[0.0 for h in range(24)] for d in range(31)]
# for i in range(31):
#     for j in range(24):
#         temps[i][j] = random.uniform(-10.0, 35.0)
# total = 0.0
# for day in temps:
#     total += day[11]
# average = total / 31
# print("the average is", average)
# highest_tem = -100.0
# for day in temps:
#     for temps in day:
#         if temps > highest_tem:
#             highest_tem = temps

# print("the highest value is", highest_tem)
# hotday = 0
# for day in temps:
#     if day[11] > 20.0:
#         hotday += 1
# print("the hotday is", hotday)
# print("the average of noon is", average)
# #################################



# building_num=3
# floar_num=15
# rooms_num=20
# rooms=[]
# list=[]
# for t in range(building_num):
#     building=[]
#     for f in range(floar_num):
#         floor=[False for f in range(rooms_num)]
#         list.append(floor)
#         building.append(rooms)
#
# rooms[2][14][2]=True
# rooms[2][14][4]=True
# rooms[2][14][7]=True
#
# vacancy=0
# for i in range (rooms_num):
#     if not rooms[2][14][i]:
#         vacancy+=1
# print("the vacancy is ",vacancy)

# #########################################
# building_num = 3
# floor_num = 15
# rooms_num = 20
#
#
# rooms = []
# for t in range(building_num):
#     building = []
#     for f in range(floor_num):
#         floor = [False for _ in range(rooms_num)]
#         building.append(floor)
#     rooms.append(building)


# rooms[2][14][2] = True
# rooms[2][14][4] = True
# rooms[2][14][7] = True
#
#
# vacancy = 0
# for i in range(rooms_num):
#     if not rooms[2][14][i]:
#         vacancy += 1
#
# print("The vacancy is", vacancy)



# list1=[1,2,3]
# list2=[]
# for v in list1:
#     list2.insert(0,v)
# print(list2)
#
# y=2+3*5.
# print(y)


##################Supersede########
# import math
# from math import pi
# result=pi
# print(result)
# pi=2.3
# print(pi)

import math


for name in dir(math):
    print(name, end="\t")

