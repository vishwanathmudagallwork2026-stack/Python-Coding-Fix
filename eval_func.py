"""Demonstrate eval() with fixed expressions and safer user input.

Never use eval() on untrusted input: it can execute arbitrary Python code.
"""

# These examples use fixed expressions for learning purposes.
result = eval("5 + 8")
print(result)
print(type(result))

a = 10
b = 20
print(a - b)

numbers = [10, 20, 30]
print(len(numbers) + 3)
print(type(()))

# Use input() for ordinary text responses instead of eval(input(...)).
citizen = input("Are you an Indian citizen? (yes/no): ").strip().lower()
if citizen in {"yes", "y"}:
    print("You answered yes.")
elif citizen in {"no", "n"}:
    print("You answered no.")
else:
    print("Please answer yes or no.")
