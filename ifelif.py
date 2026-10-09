"""Practice if/elif/else conditions with everyday examples."""

# Basic eligibility example.
age = int(input("Enter your age: "))
if age >= 18:
    print("You can apply for a licence")
else:
    print("You are not yet eligible to apply for a licence")

# Grade a student using descending thresholds.
marks = 96
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
elif marks >= 50:
    grade = "E"
else:
    grade = "F"
print(f"Grade: {grade}")

# Simple demonstration login; never hard-code real credentials.
username = "admin"
password = "1234"
if username == "admin" and password == "1234":
    print("Login successful")
elif username == "admin":
    print("Wrong password")
else:
    print("User not found")

# ATM example: do not subtract money when the withdrawal fails.
balance = 500
withdrawal = 200
if withdrawal <= 0:
    print("Withdrawal must be positive")
elif withdrawal <= balance:
    balance -= withdrawal
    print("You can withdraw the amount")
    print("Amount withdrawn:", withdrawal)
    print("Remaining balance:", balance)
else:
    print("Insufficient balance")

# Normalize case before checking the traffic-light colour.
light = "red"
light = light.strip().lower()
if light == "green":
    print("Go!")
elif light == "orange":
    print("Be ready")
else:
    print("Stop")

# Calculate an electricity bill using progressive slabs.
units = 50
if units < 0:
    raise ValueError("Units consumed cannot be negative")
if units <= 100:
    bill = units * 2
elif units <= 300:
    bill = (100 * 2) + (units - 100) * 4
else:
    bill = (100 * 2) + (200 * 4) + (units - 300) * 6

tax = bill * 0.10 if bill > 1000 else 0
final_bill = bill + tax
if units <= 100:
    category = "Low"
elif units <= 300:
    category = "Medium"
else:
    category = "High"

print(f"Units consumed: {units}")
print(f"Bill amount: {bill:.2f}")
print(f"Tax applied: {tax:.2f}")
print(f"Final bill: {final_bill:.2f}")
print(f"Usage category: {category}")
