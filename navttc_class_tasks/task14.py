# # This code cannot be terminated
# # by pressing Ctrl-C.
#
# from time import sleep
#
# seconds = 0
#
# while True:
#     try:
#         print(seconds)
#         seconds += 1
#         sleep(1)
#     except KeyboardInterrupt:
#         print("Don't do that!")

# def read_int(prompt, min, max):
#     user_input = int('enetr num=>')
#
#     if not user_input:
#         raise ValueError:
#         print('enter integer type value')
#
#     elif user_input < min and user_input > max:
#         raise except:
#         print("the value is not within permitted range enter the value again")
#
#
#
#     else:
#          return v
#
# v = read_int("Enter a number from -10 to 10: ", -10, 10)
#
# print("The number is:", v)


def read_int(prompt, min, max):
    while True:
        try:
            user_input = int(input('enter any value'))

            if user_input < min or user_input > max:
                print(f"The value is not within the permitted range ({min} to {max})"
                      f". Please enter the value again.")
            else:
                return user_input

        except ValueError:
            print("Invalid input. Please enter an integer.")


v = read_int("Enter a number from -10 to 10: ", -10, 10)
print("The number is:", v)
