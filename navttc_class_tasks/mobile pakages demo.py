def packages():
    print("\n\t\t\t\t\tsent instructions\t\t\t\t\t\t \n 1.Top Offers\n2.All in one offers\n3.supper 4G Data Offers\n4.Super Social and SMS Offers\n5.Make your own Offer\n6.My Account\n7.Jazz on WhatsApp\n8.Jazztunes\n9.VAS\n99.More")
    select_num=int(input())
    if select_num==1:
        num_1()
    elif select_num==2:
        num_2()
    elif select_num == 3:
        num_3()
    elif select_num == 4:
        num_4()
    elif select_num == 5:
        num_5()
    elif select_num == 6:
        num_6()
    elif select_num == 7:
        num_7()
    elif select_num == 9:
        num_9()
    else:
        print("invalid MMI code")
        exit()



def num_1():

    print("1.Hour 1GB @Rs.17\n3.Weekly Premium plus 5GB @Rs.304\n4.Weekly A|O@Rs.278\n6.Monthly Super Duper @Rs.1000\n7.30Day 3GB @Rs.347\n0.Back")
    select_num1=int(input())
    if select_num1==1:
        print("30 Days:10GB data,3000 Jazz Mins,300 other Network Min and 3000 SMS @Rs.1000")
    elif select_num1==3:
        print("1 Days:10GB data,@RS.90")

    elif select_num1==4:
        print("5 Days:10GB data,3000 Jazz Mins, 3000 SMS @Rs.800")
    elif select_num1==6:
        print("9 Days:10GB data,3000 Jazz Mins,300 other Network Min and 3000 SMS @Rs.800")
    elif select_num1==7:
        print("10 Days:10GB data,3000 Jazz Mins,300 other Network Min and 3000 SMS @Rs.800")
    elif select_num1==0:
       packages()
    else:
        print("invalid MMI code")
        exit()




def num_2():
    print("1.Hour 1GB @Rs.17\n3.Weekly Premium plus 5GB @Rs.304\n4.Weekly A|O@Rs.278\n6.Monthly Super Duper @Rs.1000\n7.30Day 3GB @Rs.347\n0.Back")
    select_num1=int(input())
    if select_num1==1:
        print("30 Days:10GB data,3000 Jazz Mins,300 other Network Min and 3000 SMS @Rs.1000")
    elif select_num1==3:
        print("10 Days:10GB data, @Rs.300")
    elif select_num1==4:
        print("10 Days:10GB data,3000 Jazz Mins,")
    elif select_num1==6:
        print("10 Days:10GB data,3000 Jazz Mins,300 other Network Min and 3000 SMS @Rs.800")
    elif select_num1==7:
        print("  3000 SMS @Rs.100")
    elif select_num1==0:
       packages()
    else:
        print("invalid MMI code")
        exit()

def num_3():
    print("1.Hour 1GB @Rs.17\n3.Weekly Premium plus 5GB @Rs.304\n4.Weekly A|O@Rs.278\n6.Monthly Super Duper @Rs.1000\n7.30Day 3GB @Rs.347\n0.Back")
    select_num1=int(input())
    if select_num1==1:
        print("15 Days:10GB data,3000 Jazz Mins,300 other Network Min and 3000 SMS @Rs.1000")
    elif select_num1==3:
        print("12 Days:10GB data,3000 Jazz Mins,300 other Network Min and 3000 SMS @Rs.800")
    elif select_num1==4:
        print("10 Days:10GB data,3000 Jazz Mins,300 other Network Min and 3000 SMS @Rs.800")
    elif select_num1==6:
        print("3 Days:10GB data,3000 Jazz Mins,300 other Network Min and 3000 SMS @Rs.800")
    elif select_num1==7:
        print("10 Days:10GB data,3000 Jazz Mins,300 other Network Min and 3000 SMS @Rs.800")
    elif select_num1==0:
       packages()
    else:
        print("invalid MMI code")
        exit()

def num_4():
    print("1.Hour 1GB @Rs.17\n3.Weekly Premium plus 5GB @Rs.304\n4.Weekly A|O@Rs.278\n6.Monthly Super Duper @Rs.1000\n7.30Day 3GB @Rs.347\n0.Back")
    select_num1=int(input())
    if select_num1==1:
        print("30 Days:10GB data,3000 Jazz Mins,300 other Network Min and 3000 SMS @Rs.1000")
    elif select_num1==3:
        print("10 Days:10GB data,3000 Jazz Mins,300 other Network Min and 3000 SMS @Rs.800")
    elif select_num1==4:
        print("300 other Network Min and 3000 SMS @Rs.800")
    elif select_num1==6:
        print("10 Days:10GB data,3000 Jazz Mins, @Rs.200")
    elif select_num1==7:
        print("10 Days:10GB data,3000 Jazz Mins,100 other Network Min and 3000 SMS @Rs.400")
    elif select_num1==0:
       packages()
    else:
        print("invalid MMI code")
        exit()

def num_5():
    print("1.Hour 1GB @Rs.17\n3.Weekly Premium plus 5GB @Rs.304\n4.Weekly A|O@Rs.278\n6.Monthly Super Duper @Rs.1000\n7.30Day 3GB @Rs.347\n0.Back")
    select_num1=int(input())
    if select_num1==1:
        print("30 Days:10GB data,3000 Jazz Mins,300 other Network Min and 3000 SMS @Rs.1000")
    elif select_num1==3:
        print("10 Days:10GB data,3000 Jazz Mins,300 other Network Min and 3000 SMS @Rs.800")
    elif select_num1==4:
        print("10 Days:10GB data,3000 Jazz Mins,300 other Network Min and 3000 SMS @Rs.800")
    elif select_num1==6:
        print("10 Days:10GB data,3000 Jazz Mins,300 other Network Min and 3000 SMS @Rs.800")
    elif select_num1==7:
        print("10 Days:10GB data,3000 Jazz Mins,300 other Network Min and 3000 SMS @Rs.800")
    elif select_num1==0:
       packages()
    else:
        print("invalid MMI code")
        exit()

def num_6():
    print("1.Hour 1GB @Rs.17\n3.Weekly Premium plus 5GB @Rs.304\n0.Back")
    select_num1=int(input())
    if select_num1==1:
        print("30 Days:10GB data,3000 Jazz Mins,300 other Network Min and 3000 SMS @Rs.1000")
    elif select_num1==3:
        print("10 Days:10GB data,3000 Jazz Mins,300 other Network Min and 3000 SMS @Rs.800")

    elif select_num1==0:
       packages()
    else:
        print("invalid MMI code")
        exit()

def num_7():
    print("1.Hour 1GB @Rs.17\n3.Weekly Premium plus 5GB @Rs.304\n7.30Day 3GB @Rs.347\n0.Back")
    select_num1=int(input())
    if select_num1==1:
        print("30 Days:10GB data,3000 Jazz Mins,300 other Network Min and 3000 SMS @Rs.1000")
    elif select_num1==3:
        print("10 Days:10GB data,3000 Jazz Mins,300 other Network Min and 3000 SMS @Rs.800")

    elif select_num1==7:
        print("10 Days:10GB data,3000 Jazz Mins,300 other Network Min and 3000 SMS @Rs.800")
    elif select_num1==0:
       packages()
    else:
        print("invalid MMI code")
        exit()

def num_8():
    print("1.Hour 1GB @Rs.17\n7.30Day 3GB @Rs.347\n0.Back")
    select_num1=int(input())
    if select_num1==1:
        print("30 Days:10GB data,3000 Jazz Mins,300 other Network Min and 3000 SMS @Rs.1000")

    elif select_num1==7:
        print("10 Days:10GB data,3000 Jazz Mins,300 other Network Min and 3000 SMS @Rs.800")
    elif select_num1==0:
       packages()
    else:
        print("invalid MMI code")
        exit()

def num_9():
    print("1.Hour 1GB @Rs.17\n3.Weekly Premium plus\n0.Back")
    select_num1=int(input())
    if select_num1==1:
        print("30 Days:10GB data,3000 Jazz Mins,300 other Network Min and 3000 SMS @Rs.1000")
    elif select_num1==3:
        print("10 Days:10GB data,3000 Jazz Mins,300 other Network Min and 3000 SMS @Rs.800")

    elif select_num1==0:
       packages()
    else:
        print("invalid MMI code")
        exit()




print("#"*20)
print("//Jazz packages//")
print("#"*20)
while True:
    dial=int(input("dial your code for packages"))
    if dial==433:
        packages()
    else:
        print("invalid code ")
        exit()




