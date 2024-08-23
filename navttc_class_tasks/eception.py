# try:
#     number = int(input("Enter a number: "))
#     result = 10 / number
#     print(f"The result of 10 divided by {number} is {result}")
#
# except ValueError:
#     print("Error: That's not a valid number. Please enter a valid integer.")
#
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
#
# # This block will execute no matter what
# finally:
#     print("Program execution completed.")

######################
# A program to demonstrate raising exceptions

# def calculate_square_root(number):
#     if number < 0:
#
#         raise ValueError("Cannot calculate square root of a negative number")
#
#     return number ** 0.5
#
#
# try:
#     # Take user input and convert it to a float
#     number = float(input("Enter a number: "))
#
#     # Try to calculate the square root
#     result = calculate_square_root(number)
#
#     # Print the result
#     print(f"The square root of {number} is {result}")
#
#
# except ValueError as e:
#
#     print(f"Error: {e}")
#
# finally:
#     print("Program execution completed.")
##################################################

def fun(num1,num2,operation ):
    try:
        if operation=='+':
            return num1+num2
        elif operation=='-':
            return num1-num2

        elif operation == '/':
            return num1 - num2
        else:
            raise ValueError("Cannot perform calculaion")

    except ZeroDivisionError:
        print('division by zero is not allowed')
    except ValueError as ERR:
     print("Error:",ERR)


while True:
    try:
        num1=float(input('enter 1st float number'))
        num2 = float(input('enter 1st float number'))
        operation = input('enter which operation do you want to perform number')
        fun_variable=fun(num1,num2,operation)
        print('the result after perform operation ',fun_variable)
    except ValueError:
        print('its not a valid number')
    except ZeroDivisionError:
        print('division by zero is not allowed')

    choise=input('do you want to perform the calculation again use.lower()function for input')
    if choise!='yes':
        break
    print('good bye')

















