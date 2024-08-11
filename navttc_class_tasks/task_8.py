# num1=bool(input())
# num1=bool(int(input())) #type coasting
#
#
# if num1==True:
#     print("ON")
#
#
# elif num1==False:
#     print("OFF")
# else:
#     exit()

# num1=50
# num2=40
# graeter = num1 >= num2
#
#
# if graeter:
#  print("the value is greater")
# else:
#     print("false")

# user=int("enter any value")  # without ifelse
# num=100
# compare=user<=num
# print()

# def go_for_walk():
#     print("the weather is good go for a walk")
#
# def stay_home():
#     print("the weather is bad so stay home")
#
# def lunch():
#     print("let\'s have a lunch")
#
# user=input("enetr about weather is it good or bad")
#
# if user=='good':
#     go_for_walk()
# elif user=='bad':
#     stay_home()
# else:
#  print("weather not define")
#
# lunch()

def sheep_com():
    print("your sheeps is completed \n make a bed\n Take a shower and sleep")
def sheep_missing():
    print("your sheep is not completed")
def search():
    print("search your sheeps")
def feed():
    print("feed the sheepdogs")

sheeps=int(input("enter the number of sheeps"))
if sheeps>=120:
    sheep_com()
elif sheeps<=120:
    sheep_missing()
    search()
else:
    exit()

feed()








