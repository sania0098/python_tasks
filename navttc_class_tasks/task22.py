# class MyZeroDivisionError(ZeroDivisionError):
#     pass
#
#
# def do_the_division(mine):
#     if mine:
#         raise MyZeroDivisionError("some worse news")
#     else:
#         raise ZeroDivisionError("some bad news")
#
#
# for mode in [False, True]:
#     try:
#         do_the_division(mode)
#     except ZeroDivisionError:
#         print('Division by zero')
#
# for mode in [False, True]:
#     try:
#         do_the_division(mode)
#     except MyZeroDivisionError:
#         print('My division by zero')
#     except ZeroDivisionError:
#         print('Original division by zero')
#####################











# Custom Exceptions
class MyZeroDivisionError(ZeroDivisionError):
    pass

class MyOverflowError(OverflowError):
    pass

class MyUnderflowError(Exception):
    pass


# Function to test for exceptions
def test_value(value):
    if value == 0:
        raise MyZeroDivisionError("Zero division occurred")
    elif value > 100:
        raise MyOverflowError("Value exceeds the upper limit")
    elif value < 0:
        raise MyUnderflowError("Negative value provided")
    else:
        return 100 / value  # For non-exceptional cases


# Loop to test all possible error scenarios
test_values = [-10, 0, 50, 150]  # Testing a negative value, zero, valid value, and overflow

for value in test_values:
    try:
        result = test_value(value)
        print(f"Result of division: {result}")
    except MyZeroDivisionError as zde:
        print(f"Caught MyZeroDivisionError: {zde}")
    except MyOverflowError as ofe:
        print(f"Caught MyOverflowError: {ofe}")
    except MyUnderflowError as ufe:
        print(f"Caught MyUnderflowError: {ufe}")
    except ZeroDivisionError as zde:
        print(f"Caught standard ZeroDivisionError: {zde}")
    except OverflowError as ofe:
        print(f"Caught standard OverflowError: {ofe}")
    except Exception as e:
        print(f"Caught an unexpected error: {e}")




















