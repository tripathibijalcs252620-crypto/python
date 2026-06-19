import math

while True:
    try:
        num = float(input("Enter a number: "))

        if num < 0:
            print("Square root of a negative number is not possible.")
        else:
            result = math.sqrt(num)
            print("Square root =", result)

    except ValueError:
        print("Invalid input! Please enter a valid number.")

    choice = input("Do you want to continue? (yes/no): ").lower()
    if choice != "yes":
        break

print("Program ended.")
