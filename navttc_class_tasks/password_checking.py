Define_password="pythonRocks"
max_attem=5
attempts=0
while attempts<max_attem:

    password=input("eenter assword is=")
    if password==Define_password:
        print("password accepted")
        exit()
    else:
       attempts+=1
       remaining_attemps=max_attem-attempts
       print("incorrect password")
    if attempts==max_attem:
           print("sorry you have run out of attempts")
           exit()


