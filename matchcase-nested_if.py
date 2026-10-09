"""Practice match/case and nested loops (Python 3.10+)."""

try:
    day_number = int(input("Enter a day number (1-7): "))
except ValueError:
    print("Please enter a whole number from 1 to 7.")
else:
    match day_number:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            # A wildcard is the correct catch-all pattern in match/case.
            print("Invalid day")

# Nested loops: print values from the inner range for every outer value.
for outer_number in range(3, 6):
    for inner_number in range(8, 11):
        print(f"outer={outer_number}, inner={inner_number}")
