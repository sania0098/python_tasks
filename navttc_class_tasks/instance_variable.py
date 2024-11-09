##### LAB 1
# class Timer:
#     def __init__(self, hours=0, minutes=0, seconds=0):
#         self.__hours = hours
#         self.__minutes = minutes
#         self.__seconds = seconds
#
#     def __str__(self):
#         # Return the time in "hh:mm:ss" format with leading zeros
#         return f"{self.__hours:02}:{self.__minutes:02}:{self.__seconds:02}"
#     #The :02 format specifier ensures that the hours, minutes,
#     # and seconds are printed with leading zeros when they are less than 10 (e.g., 02 for 2).
#
#
#     def next_second(self):
#         # Increment time by 1 second, handle overflow to minutes and hours
#         self.__seconds += 1
#         if self.__seconds == 60:
#             self.__seconds = 0
#             self.__minutes += 1
#             if self.__minutes == 60:
#                 self.__minutes = 0
#                 self.__hours += 1
#                 if self.__hours == 24:
#                     self.__hours = 0
#
#     def prev_second(self):
#         # Decrement time by 1 second, handle underflow from minutes and hours
#         self.__seconds -= 1
#         if self.__seconds == -1:
#             self.__seconds = 59
#             self.__minutes -= 1
#             if self.__minutes == -1:
#                 self.__minutes = 59
#                 self.__hours -= 1
#                 if self.__hours == -1:
#                     self.__hours = 23
#
#
# # Testing the Timer class
# timer = Timer(23, 59, 59)
# print(timer)           # Expected: 23:59:59
# timer.next_second()
# print(timer)           # Expected: 00:00:00
# timer.prev_second()
# print(timer)           # Expected: 23:59:59




###########LAB 2
# class WeekDayError(Exception):
#     pass
#
# class Weeker:
#     # List of valid days
#     __days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
#
#     def __init__(self, day):
#         if day not in Weeker.__days:
#             raise WeekDayError  # Raise exception if the day is not valid
#         self.__current_day = day  # Store the current day as a private attribute
#
#     def __str__(self):
#         return self.__current_day  # Return the current day as a string
#
#     def add_days(self, n):
#         # Find the index of the current day and add 'n' days, wrapping using modulo
#         current_index = Weeker.__days.index(self.__current_day)
#         new_index = (current_index + n) % 7
#         self.__current_day = Weeker.__days[new_index]
#
#     def subtract_days(self, n):
#         # Find the index of the current day and subtract 'n' days, wrapping using modulo
#         current_index = Weeker.__days.index(self.__current_day)
#         new_index = (current_index - n) % 7
#         self.__current_day = Weeker.__days[new_index]
#
# # Test the class with the expected output
# try:
#     weekday = Weeker('Mon')
#     print(weekday)  # Expected: Mon
#     weekday.add_days(15)
#     print(weekday)  # Expected: Tue
#     weekday.subtract_days(23)
#     print(weekday)  # Expected: Sun
#     weekday = Weeker('Monday')  # This will raise an exception
# except WeekDayError:
#     print("Sorry, I can't serve your request.")
#
#
# ###############LAB 3
# import math
#
# class Point:
#     def __init__(self, x=0.0, y=0.0):
#         # Store coordinates as private attributes
#         self.__x = float(x)
#         self.__y = float(y)
#
#     def getx(self):
#         # Return the x coordinate
#         return self.__x
#
#     def gety(self):
#         # Return the y coordinate
#         return self.__y
#
#     def distance_from_xy(self, x, y):
#         # Calculate the distance between the current point and the given (x, y)
#         return math.hypot(self.__x - x, self.__y - y)
#
#     def distance_from_point(self, point):
#         # Calculate the distance between the current point and another Point object
#         return math.hypot(self.__x - point.getx(), self.__y - point.gety())
#
# # Test the class
# point1 = Point(0, 0)
# point2 = Point(1, 1)
# print(point1.distance_from_point(point2))  # Expected: 1.4142135623730951
# print(point2.distance_from_xy(2, 0))      # Expected: 1.4142135623730951
#
#
#
# ##################LAB 4
# import math
#
# class Point:
#     def __init__(self, x=0.0, y=0.0):
#         self.__x = float(x)
#         self.__y = float(y)
#
#     def getx(self):
#         return self.__x
#
#     def gety(self):
#         return self.__y
#
#     def distance_from_xy(self, x, y):
#         return math.hypot(self.__x - x, self.__y - y)
#
#     def distance_from_point(self, point):
#         return math.hypot(self.__x - point.getx(), self.__y - point.gety())
#
#
# class Triangle:
#     def __init__(self, vertice1, vertice2, vertice3):
#         # Storing the vertices as a private list
#         self.__vertices = [vertice1, vertice2, vertice3]
#
#     def perimeter(self):
#         # Calculate the perimeter by summing up the distances between vertices
#         v1, v2, v3 = self.__vertices
#         # Distance between vertice1 and vertice2
#         side1 = v1.distance_from_point(v2)
#         # Distance between vertice2 and vertice3
#         side2 = v2.distance_from_point(v3)
#         # Distance between vertice3 and vertice1
#         side3 = v3.distance_from_point(v1)
#         # Return the perimeter
#         return side1 + side2 + side3
#
#
# # Test the Triangle class
# triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
# print(triangle.perimeter())  # Expected: 3.414213562373095
