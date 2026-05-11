# Basic Exception Handling

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")


# Multiple Except Blocks

try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

# Catching Multiple Exceptions Together

try:
    value = int(input("Enter a number: "))
    result = 10 / value
except (ValueError, ZeroDivisionError) as e:
    print(f"An error occurred: {e}")


# The else Clause

try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Division successful!", result)


# The finally Clause

try:
    file = open("data.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Execution completed.")


# Raising Exceptions

try:
    value = -10

    if value < 0:
        raise ValueError("value cannot be negative.")

except ValueError as e:
    print(e)

# Custom Error Messages:

try:
    raise Exception("Custom error message")

except Exception as e:
    print(e)


# Custom Exceptions

class NegativeValueError(Exception):
    pass
try:
    value = -5

    if value < 0:
        raise NegativeValueError("Negative values are not allowed.")

except NegativeValueError as e:
    print(e)

# Real-world Example

class InsufficienceBalanceError(Exception):
    pass
    
try:
    balance = 500
    withdraw = 1000

    if withdraw > balance:
        raise InsufficienceBalanceError("not enough balance.")

except InsufficienceBalanceError as e:
    print(e)
    
    

# Nested Exception Handling

try:
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Handled division by zero inside nested try block.")
except Exception as e:
    print(e)
