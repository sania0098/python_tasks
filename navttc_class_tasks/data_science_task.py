import numpy as num
import matplotlib.pyplot as mat
from matplotlib import style
import random


#  the use of scatter (dots graph)

# x_data=num.random.random(5000)*100
# y_data=num.random.random(5000)*100
# mat.scatter(x_data,y_data,c='green',marker='*',alpha=0.3)
# mat.show()



# the use of plot(draw lines instead of dots)

# years=[2006 + x for x in range(16)]
# weight=[23,89,86,45,67,56,45,98,23,12,88,89,65,38,96,12]
# mat.plot(years,weight,lw=2,c='b',linestyle='--')
# mat.show()

# the use of bar

# courses=["java","c++","abject_oriented","python","dart"]
# votes=[55,70,16,99,39]
# mat.bar(courses,votes,color="red",align='edge',
#         width=0.3,edgecolor="green",lw=10)  # here the align edge show the starting point of bar
# mat.show()

#########
# ages=num.random.normal(16,7.9,2000)
# # mat.hist(ages,bins=20) # specify number of bins
# # mat.hist(ages,bins=[ages.1, ages.max()]min(),16,21,ages.max()]) #to specify specific bins
# mat.hist(ages, bins=20,
#          cumulative=True)
#
#
# mat.show()

############
#All about pie chart
# courses= ["java","c++","abject_oriented","python","dart"]
# votes= [55,70,16,99,39]
# drag_out=[0.5,0,0,0,0]
# # to drag out any side from the pie chat use explode=variable name
# # autopct used to see percentage of each slice
# #pctdistance is used for angle distance from center
# #start angle used to specify starting angle
# mat.pie(votes,labels=courses,explode=drag_out,
#         autopct='%.5f%%',pctdistance=1.5,startangle=90)
# mat.show()
#################

# hight=num.random.normal(122,80,200)
# mat.boxplot(hight)
# mat.show()
###############
#The example of boxplot

# num1=num.linspace(0,17,27)
# num2=num.linspace(322,69,17)
# num3=num.linspace(219,47,47)
# num4=num.linspace(342,17,27)
# data=num.concatenate((num1,num2,num3,num4)) #without concatenation 4 diff boxplot are shown so we can first concatinate all the boxes than sho
# mat.boxplot(data)
# mat.show()
##############



# years=[2010,2011,2012,2012,2013,2014,2015,2016,2017,2018,2019,2020]
# income=[23,56,44,55,66,99,76,56,88,98,34,99]
# income_ticks=list(range(23,87,9))
# mat.plot(years,income)
# mat.title("record of ali for the year 2010 to 2020",fontsize=20,fontname='arial')
# mat.xlabel('record of income')
# mat.ylabel("years")
# mat.yticks(income_ticks,[f"{x}k usd" for x in income_ticks])
#
# mat.show()
#####################

# stock1=[102,912,189,13,141,115,661]
# stock2=[98,92,199,113,114,15,66]
# stock3=[202,112,124,127,114,175,616]
# mat.plot(stock1,label="campany1")
# mat.plot(stock2,label="campany2")
# mat.plot(stock3,label="campany3")
# mat.legend()        #without legent labels can't shown
# # mat.legend(loc='lower center') # also specify location
# mat.show()
####################3


#  # Lableling of the piechart
# style.use("dark_background")
# # style.use("ggplot")
# votes=[12,31,8,33,76]
# public=['a','b','c','d','e']
#
# mat.pie(votes,labels=None)
# mat.legend(labels=public)
# mat.show()

#######################

# x1,y1=num.random.random(100),num.random.random(100)
# x2,y2=num.random.random(100),num.random.random(100)
# mat.figure(1)
# mat.scatter(x1,y1)
# mat.figure(2)
# mat.plot(x2,y2)
# mat.show()
###############

# x=num.arange(100)
# fig,axs=mat.subplots(2,2)  #for 2 rows and 2 columns
#
# axs[0,0].plot(x,num.sin(x))
# axs[0,0].set_title("sine wave")
#
# axs[0,1].plot(x,num.sin(x))
# #row 0,  column 1
# axs[0,1].set_title('cosine wave')
#
# axs[1,0].plot(x,num.random.random(100))
# axs[1,0].set_title('random function')
#
# axs[1,1].plot(x,num.log(x))
# axs[1,1].set_title('log function')
# fig.suptitle("four plotes")
# mat.show()
#
# mat.savefig("4fih_png",dpi=300,transparent=True,bbox_inches="tight")
#######################################################################################
#the 3 dimention chart

# ax=mat.axes(projection='3d')
# x=num.random.random(100)
# y=num.random.random(100)
# z=num.random.random(100)
#
# ax.scatter(x,y,z)
# ax.set_title("3D plot")
# ax.set_xlabel('test')
# mat.show()



# ax=mat.axes(projection='3d')
# x=num.arange(0,50,0.1)
# # y=num.sin(x)
# y=num.arange(0,50,0.1)
# # z=num.cos(x)
# z=num.cos(x+y)
#
# ax.plot(x,y,z)
# ax.set_title("3D plot")
# ax.set_xlabel('test')
# mat.show()
###########################
# ax=mat.axes(projection='3d')
# num1=num.arange(-5,5,0.1)
#
# num2=num.arange(-5,5,0.1)
#
# X,Y=num.meshgrid(num1,num2)
# Z=num.meshgrid(num1)* num.cos(num2)
# ax.plot_surface(X,Y,Z,cmap="Accent_r")  #cmap is used for coloring
# ax.set_title("3D plot")
# ax.set_xlabel('test')
# mat.show()
#######################

# heads_tails=[0,0]
# for _ in range(100000):
#     heads_tails[random.randint(0,1)]  +=1
#     mat.bar(["heads","tails"],heads_tails,color=["red","blue"])
#     mat.pause(0.001)
# mat.show()


