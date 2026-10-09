"""Examples of assignment, identity, membership, and basic operators."""

# Assignment operators update a variable using its current value.
x = 7
n = 5
x += n
print("After addition:", x)
x -= n
print("After subtraction:", x)
x *= n
print("After multiplication:", x)
x /= n
print("After division:", x)
x //= 7
print("After floor division:", x)
x %= n
print("After modulus:", x)

# Identity checks whether two names refer to the same object.
fruits_a = ["apple", "banana", "cat"]
fruits_b = fruits_a
fruits_c = ["apple", "banana", "cat"]
print(fruits_a is fruits_b)  # True: both names refer to one list.
print(fruits_a == fruits_c)  # True: the list contents are equal.
print(fruits_a is fruits_c)  # False: these are separate list objects.

# Membership operators check whether a value is in a collection.
animals = ["cats", "balls", "bat"]
items = ["banana", "Bunk", "bat1"]
print("cats" in animals)
print("bat1" in items)
print("balling" not in animals)
print("A" in "Amazon")

# Example: bill calculator with a flat discount.
price = 499
quantity = 4
flat_discount = 10
total = price * quantity - flat_discount
print(f"Total after flat discount: {total}")

# Example: odd or even.
number = 90
print("Even" if number % 2 == 0 else "Odd")

# Demonstration only; production apps should never hard-code credentials.
username = "admin"
password = "1234"
is_valid_login = username == "admin" and password == "1234"
print("Login successful" if is_valid_login else "Invalid credentials")

# Apply a 10% discount only when the total exceeds 1,000.
apple_price = 300
banana_price = 500
cover_price = 400
total_price = apple_price + banana_price + cover_price
discount_rate = 0.10 if total_price > 1000 else 0.0
after_discount = total_price * (1 - discount_rate)

print(f"Total before discount: {total_price:.2f}")
print(f"Discount: {total_price * discount_rate:.2f}")
print(f"Total after discount: {after_discount:.2f}")
print("Premium customer" if total_price > 1000 else "Regular customer")
