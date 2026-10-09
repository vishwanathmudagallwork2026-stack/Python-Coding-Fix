"""A simple command-line calculator for four arithmetic operations."""


def main():
    """Read an operation and two numbers, then display the result."""
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        choice = int(input("Enter your choice (1-4): "))
        if choice not in (1, 2, 3, 4):
            print("Invalid choice. Select a number from 1 to 4.")
            return
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Enter a whole-number choice and valid numbers.")
        return

    if choice == 1:
        result = num1 + num2
    elif choice == 2:
        result = num1 - num2
    elif choice == 3:
        result = num1 * num2
    else:
        # The second number is the divisor; check it before dividing.
        if num2 == 0:
            print("Cannot divide by zero.")
            return
        result = num1 / num2

    print(f"Result: {result:g}")


if __name__ == "__main__":
    main()
