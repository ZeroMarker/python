numbers = [1, 2]

# print(numbers[2])
try:
    with open("guess.py") as file:
        print("File opened.")
    age = int(input("Input your age:"))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError, FileNotFoundError):
    print("You didn't input a valid age.")
except ValueError as ex:
    print("You didn't input a valid age.")
    print(ex)
    print(type(ex))
except ZeroDivisionError as ze:
    print("Age cannot be zero.")
    print(ze)
    print(type(ze))
else:
    print(f"Age = {age}.\n", "No exception occurred.")
finally:
    print("Nothing to do.")


def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)

