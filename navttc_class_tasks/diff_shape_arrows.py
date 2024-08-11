def square():
 print("SQUARE")
 print("*"*25)
 print("\t\t\t\t\t\t\n*\t\t\t\t\t\t*\n*\t\t\t\t\t\t*\n*\t\t\t\t\t\t*\n*\t\t\t\t\t\t*\n*\t\t\t\t\t\t*\n*\t\t\t\t\t\t*\n*\t\t\t\t\t\t* ")
 print("*"*25)

def  triangle():
 print("TRIANGLE")
 print("##\n#\t#\n#\t\t#\n#\t\t\t#\n#\t\t\t\t#\n#\t\t\t\t\t#\n#\t\t\t\t\t\t#\n#\t\t\t\t\t\t\t#\n#","#"*27)

def circle():
 print("CIRCLE")
 print("    *\n \t\t  *\n\t\t\t\n*\t\t\t*\n \t\t   *\n    ***")

def rectangle():
 print("RECTANGLE")
 print("*"*41)
 print("\t\t\t\t\t\t\t\t\t\t\n*\t\t\t\t\t\t\t\t\t\t*\n*\t\t\t\t\t\t\t\t\t\t*\n*\t\t\t\t\t\t\t\t\t\t*\n*\t\t\t\t\t\t\t\t\t\t*\n*\t\t\t\t\t\t\t\t\t\t*\n*\t\t\t\t\t\t\t\t\t\t*\n*\t\t\t\t\t\t\t\t\t\t* ")
 print("*"*41)

def pentagon():
 print("PENTAGON")
 print("\t\t\t ^^^^^^^^\n\t\t   ^\t\t   ^\n\t\t ^\t\t\t\t ^\n\t\t^\t\t\t      ^\n\t\t  ^\t\t\t    ^\n\t\t\t^\t\t  ^\n\t\t\t  ^^^^^^^")

while True:
     print("5 types of shaps are availible \n press 1. for square shape\n press 2. for triangular shape\n press 3. for circle shape\n press 4. for rectangle shape\n press 5.for pentagon")
     choice=int(input("Enter your choice"))
     if choice==1:
         square()
         print("Thank you")
     elif choice==2:
         triangle()
         print("Thank you")
     elif choice==3:
         circle()
         print("Thank you")
     elif choice==4:
         rectangle()
         print("Thank you")
     else:
         pentagon()
         print("Thank you")