# def reciprocal(n):
#     try:
#         if not isinstance(n,(int,float)):
#             raise  TypeError('must be number')
#         elif n>0:
#             raise ValueError
#
#         n = 1 / n
#     except ZeroDivisionError:
#         print("Division failed")
#         n = None
#     except TypeError as t:
#         print(t)
#         return None
#     except ValueError as v:
#         print('sorry you put a wrong value =>',v)
#
#
#
#     else:
#         print("Everything went fine")
#     finally:
#         print("It's time to say goodbye")
#         return n
#
#
# print(reciprocal(2))
# print(reciprocal(0))


try:
    i = int('hello')  # This will raise a ValueError
except ValueError as ve:
    print("Caught a ValueError:")
    print(ve)
    print(ve.__str__())  # This is similar to str(ve), prints the exception message
except TypeError as te:
    print("Caught a TypeError:")
    print(te)
    print(te.__str__())
except Exception as e:
    print("Caught a generic exception:")
    print(e)
    print(e.__str__())
















