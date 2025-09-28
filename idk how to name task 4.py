while True:
    try:
        num1 = int(input("Please enter the first number: "))
        num2 = int(input("Please enter the second number: "))
        num3 = int(input("Please enter the third number: "))

        print(f"Sum: {num1 + num2 + num3}\n"
                  f"Product: {num1 * num2 * num3}\n"
                  f"Average: {(num1 + num2 + num3)/3}\n")
    except ValueError:
        print(f"Error. Please enter a valid numerical value for all given inputs.")
