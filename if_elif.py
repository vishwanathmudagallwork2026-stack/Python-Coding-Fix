"""Practice chained conditions, nested conditions, and ATM withdrawal logic."""


def describe_age(age):
    """Return an age category without overlapping boundary conditions."""
    if not 1 <= age <= 120:
        return "Invalid age"
    if age <= 12:
        return f"{age} is the age of a child"
    if age <= 17:
        return f"{age} is the age of a teenager"
    if age <= 30:
        return f"{age} is the age of a young adult"
    if age <= 60:
        return f"{age} is the age of a working adult"
    return f"{age} is the age of a senior adult"


try:
    age = int(input("Enter your age: "))
    print(describe_age(age))
except ValueError:
    print("Please enter age as a whole number.")

# Simple comparison example.
a = 30
b = 300
print(f"{b} is greater than a" if b > a else f"{b} is not greater than a")

# Nested if/else example for a signed number.
number = -8
if number >= 0:
    print("The number is zero" if number == 0 else "The number is positive")
else:
    print("The number is negative")

grade = 40
print("Pass" if grade >= 50 else "Fail")

# ATM example: update the balance only if the withdrawal is valid.
try:
    balance = float(input("Enter the balance: "))
    withdrawal = float(input("Enter the withdrawal amount: "))
    if balance < 0 or withdrawal <= 0:
        print("Balance cannot be negative and withdrawal must be positive.")
    elif withdrawal <= balance:
        balance -= withdrawal
        print("Withdrawal successful")
        print(f"Remaining balance: {balance:.2f}")
    else:
        print("Insufficient balance; account balance remains unchanged.")
except ValueError:
    print("Please enter valid numeric amounts.")
