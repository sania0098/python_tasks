class CustomError(Exception):
    def __init__(self, message, code, severity):
        self.message = message
        self.code = code
        self.severity = severity
        # Initialize the base Exception class with a tuple of these arguments
        super().__init__(message, code, severity)

    # Overriding __str__ to provide a custom error message
    def __str__(self):
        return f"[{self.severity} Severity] Error {self.code}: {self.message}"


def print_args(args):
    lng = len(args)
    if lng == 0:
        print("")
    elif lng == 1:
        print(args[0])
    else:
        print(str(args))


# Example 1: Raise a generic exception
try:
    raise Exception
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)

# Example 2: Raise a generic exception with a custom message
try:
    raise Exception("my exception")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)

# Example 3: Raise a generic exception with multiple arguments
try:
    raise Exception("my", "exception")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)

# Example 4: CustomError with message, code, and severity
try:
    raise CustomError("Custom exception occurred", 404, "High")
except CustomError as e:
    # Print the exception in a formatted way
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)
