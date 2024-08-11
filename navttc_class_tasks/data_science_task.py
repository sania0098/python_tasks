import numpy as num
import matplotlib.pyplot as mat


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