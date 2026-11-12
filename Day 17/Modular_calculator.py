import math

def add(num1 : float, num2 : float) -> float:

    """Add the two numbers"""

    return num1 + num2

def sub(num1 : float, num2 : float) -> float:

    """Subtract the two numbers"""

    return num1 - num2

def mul(num1 : float, num2 : float) -> float:

    """Multiply the two numbers"""

    return num1 * num2

def divide(num1 : float, num2 : float) -> float:

    """Divide the two numbers"""

    if num2 == 0:

        raise ZeroDivisionError("Cannot Divide by zero")

    return num1 / num2

def power(base : float, exp : float) -> float:

    """Returns the result of base with the power exp"""

    return math.pow(base, exp)

def square_root(num : float) -> float:

    """Returns the square root of the number"""

    if num < 0:

        raise ValueError("Cannot find the square root of negative numbers")
    
    return math.sqrt(num)

def logarithm(num : float, base : float = math.e) -> float: #takes eulers number as base by default if not specified

    """Log num with base"""

    if num <= 0:

        raise ValueError("Logarithm number must be greater then zero")

    if base <= 0 or base == 1:

        raise ValueError("Invalid Base")

    return math.log(num, base)

while True:

    #menu
    print(f"""

            {"=" * 30}
            0.Exit
            1.Addition
            2.Subtraction
            3.Multiply
            4.Divide
            5.Power
            6.Square root
            7.Logarithm
            {"=" * 30 }\n

    """)

    try:

        choice = int(input("Enter your choice: "))

    except ValueError:

        print("Choose from the above option only")

        continue

    if choice < 0 or choice > 7:

        print("Invalid option: Choose from the above options")

        continue

    match choice:

        case 0:

            print("Thank you for using our program!\n")

            break

        case 1:

            try: 

                num1 = float(input("Enter the first number: "))

                num2 = float(input("Enter the second number: "))

            except ValueError:

                print("ValueError: Enter the value in float data type")

                continue

            print(f"Addition: {add(num1, num2)}")

        case 2:

            try: 

                num1 = float(input("Enter the first number: "))

                num2 = float(input("Enter the second number: "))

            except ValueError:

                print("ValueError: Enter the value in float data type")

                continue

            print(f"Subtraction: {sub(num1, num2)}")

        case 3: 

            try: 

                num1 = float(input("Enter the first number: "))

                num2 = float(input("Enter the second number: "))

            except ValueError:

                print("ValueError: Enter the value in float data type")

                continue

            print(f"Multiplication: {mul(num1, num2)}")

        case 4: 

            try: 

                num1 = float(input("Enter the first number: "))

                num2 = float(input("Enter the second number: "))

            except ValueError:

                print("ValueError: Enter the value in float data type")

                continue

            print(f"Divide: {divide(num1, num2)}")

        case 5:

            try: 

                base = float(input("Enter the base: "))

                exp = float(input("Enter the exponent: "))

            except ValueError:

                print("ValueError: Enter the value in float data type")

                continue

            print(f"Answer: {power(base, exp)}")

        case 6:

            try: 

                num = float(input("Enter the number: "))

            except ValueError:

                print("ValueError: Enter the value in float data type")

                continue

            print(f"Square root: {square_root(num)}")

        case 7:

            try: 

                num = float(input("Enter the number: "))

                base = float(input("Enter the base: "))

            except ValueError:

                print("ValueError: Enter the value in float data type")

                continue

            print(f"Answer: {logarithm(num, base)}")