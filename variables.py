"""Examples of variables, Boolean values, and while loops."""

name = "Vishwanath"
age = 21
print(f"{name} is {age} years old")

is_online = True
is_offline = False
is_running = True
print(f"Are you online? {is_online}")
print(f"Are you offline? {is_offline}")
print(f"Is the program running? {is_running}")

# Stop each loop once its counter reaches the target.
count = 0
while True:
    print(count)
    count += 1
    if count == 10:
        break

count = 0
while True:
    print(count)
    count += 1
    if count == 5:
        break
