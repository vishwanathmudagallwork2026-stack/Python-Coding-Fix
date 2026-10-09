"""Examples of reading and converting user input."""


def main():
    """Collect text, integer, and floating-point input."""
    name = input("Enter your name: ").strip()

    try:
        age = int(input("Enter your age: "))
        height = float(input("Enter your height in cm: "))
    except ValueError:
        print("Please enter a whole number for age and a number for height.")
        return

    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Height: {height} cm")
    print(f"Height data type: {type(height).__name__}")

    print("This program checks a self-reported citizenship answer.")
    citizen = input("Are you an Indian citizen? (yes/no): ").strip()
    print(f"Answer: {citizen}")
    print(f"Answer data type: {type(citizen).__name__}")


if __name__ == "__main__":
    main()
