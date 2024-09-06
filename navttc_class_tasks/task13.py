# path=input('enetr path ')
# def fun(a):
#     var=a.rfind('/')
#     if var!=-1:
#         var2=path[var+1:]
#     else:
#         var2=path
#
#     if not var2:
#         return  "file not found"
#     return var2
#
#
#
# fun(path)

# file=input('enter the  values=>')
# if (file.startswith("data") or file.endswith("file.pdf")
#         or file.startswith('image.jpeg') and file.endswith('file.pdf')):
#     print('true')
# else:
#     print('false')


# def mysplit(string):
#     list=[]
#     var=''
#     for ch in string:
#         if ch=='':
#             if var:
#                 list.append(var)
#                 var=''
#         else:
#             var+=ch
#
#
#
#     if var:
#         list.append(var)
#         return list
# # print(mysplit('To be or not to be, that is the question'))
# # print(mysplit('To be or not to be,that is the question'))
# # print(mysplit(''))
# # print(mysplit('abc'))
# # print(mysplit(' '))
# string=input('enetr your string; ')
# print(mysplit(string))


#####################The Caesar Cipher: decrypting a message
# cipher = input('Enter your cryptogram: ')
# text = ''
# for char in cipher:
#     if not char.isalpha():
#         continue
#     char = char.upper()
#     code = ord(char) - 1
#     if code < ord('A'):
#         code = ord('Z')
#     text += chr(code)
#
# print(text)


######################CEASER CIPHER :ENCRYPTION
 
# # Caesar cipher.
# text = input("Enter your message: ")
# cipher = ''
# for char in text:
#     if not char.isalpha():
#         continue
#     char = char.upper()
#     code = ord(char) + 1
#     if code > ord('Z'):
#         code = ord('A')
#     cipher += chr(code)
#
# print(cipher)

###############The Numbers Processor
# Numbers Processor.

# line = input("Enter a line of numbers - separate them with spaces: ")
# strings = line.split()
# total = 0
# try:
#     for substr in strings:
#         total += float(substr)
#     print("The total is:", total)
# except:
#     print(substr, "is not a number.")



#############
# IBAN Validator.

# iban = input("Enter IBAN, please: ")
# iban = iban.replace(' ','')

# if not iban.isalnum():
#     print("You have entered invalid characters.")
# elif len(iban) < 15:
#     print("IBAN entered is too short.")
# elif len(iban) > 31:
#     print("IBAN entered is too long.")
# else:
#     iban = (iban[4:] + iban[0:4]).upper()
#     iban2 = ''
#     for ch in iban:
#         if ch.isdigit():
#             iban2 += ch
#         else:
#             iban2 += str(10 + ord(ch) - ord('A'))
#     iban = int(iban2)
#     if iban % 97 == 1:
#         print("IBAN entered is valid.")
#     else:
#         print("IBAN entered is invalid.")

###############task1
# def fun(par1,par2):
#     string=''
#     var_shift=var2%26
#     for a in var1:
#         if a.isalpha():
#             if a.lower():
#                 base=ord('a')
#             else:
#                 base=ord('A')
#             new=chr((ord(a)-base+var2)%26+base)
#             string+=new
#         else:
#             string+=a
#         return string
#
#
# var1=input('enter =>')
# while True:
#     try:
#         var2=int(var1)
#         print('limit should not exceed than 25')
#         if var2<=1 or  var2>=25:
#             break
#         else:
#             print('Enter a valid number')
#
#     except ValueError:
#         print('invalid input please enter the integer again')
#
#
# fun_variable=fun(var1,var2)
# print(fun_variable)






# def fun(par1, par2):
#     string = ''
#     var_shift = par2 % 26
#     for a in par1:
#         if a.isalpha():
#             if a.islower():
#                 base = ord('a')
#             else:
#                 base = ord('A')
#             new = chr((ord(a) - base + var_shift) % 26 + base)
#             string += new
#         else:
#             string += a
#     return string
#
# var1 = input('Enter a string: ')
# while True:
#     try:
#         var2 = int(input('limit should not exceed than 25=> '))
#         if var2 <= 1 or var2 >= 25:
#             break
#         else:
#             print('enter a valid number=>')
#     except ValueError:
#         print('Invalid input. Please enter an integer again=>.')
#
# fun_variable = fun(var1, var2)
# print(fun_variable)


###################PALANDROME


#
# user_input = input('Enter a name to check if it is a palindrome or not: ')
# user_input = user_input.replace(' ', '').lower()
#
# if not user_input:
#     print('Not a palindrome')
# else:
#     if user_input == user_input[::-1]:
#         print("=> It's a palindrome")
#     else:
#         print('Not a palindrome')

################ANAGRAM

# str1=input("enter 1st string")
# str2=input('enetr 2nd string')
# str1 = str1.replace(' ', '').lower()
# str2 = str2.replace(' ', '').lower()
# new_str1=sorted(str1)
# new_str2=sorted(str2)
# if  new_str1 == new_str2:
#     print("its anagram")
# else:
#     print('not an anagram')



#######






# def fun(par):
#     emp_string=''
#     normalized = emp_string.join(filter(str.isdigit, par))
#     def sum_of_digits(num):
#             return sum(int(digit) for digit in str(num))
#     result = sum_of_digits(normalized)
#     while result >= 10:
#         result = sum_of_digits(result)
#     return result
# DOB = input('enter data in the form of YYYYMMDD=>') # Example input
# final_result = fun(DOB)
# print("The reduced single digit is:", final_result)


##################characters comprising the first string hidden inside the second string?

# def is_hidden(word, string):
#
#     current_pos = 0
#
#
#     for char in word:
#
#         found_pos = string.find(char, current_pos)
#
#
#         if found_pos == -1:
#             return False
#
#
#         current_pos = found_pos + 1
#
#
#     return True
# word = input("enter word which you have to find")
# string = input('enetr string from wich you find word')
# print(is_hidden(word, string))  # Expected output: True




def is_valid_sudoku(board):
    # Function to check if a list contains all digits from 1 to 9
    def check_group(group):
        return sorted(group) == list('123456789')

    # Check all rows
    for row in board:
        if not check_group(row):
            return False

    # Check all columns
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if not check_group(column):
            return False

    # Check all 3x3 sub-squares
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            sub_square = []
            for r in range(3):
                for c in range(3):
                    sub_square.append(board[box_row + r][box_col + c])
            if not check_group(sub_square):
                return False

    # If all checks passed
    return True

# Input
board = []
print("Enter the Sudoku board row by row (9 rows with 9 digits each):")
for _ in range(9):
    row = input().strip()
    if len(row) != 9 or not row.isdigit():
        print("Invalid input. Please enter exactly 9 digits.")
        exit(1)
    board.append(list(row))

# Validate and output the result
if is_valid_sudoku(board):
    print("Yes")
else:
    print("No")






























