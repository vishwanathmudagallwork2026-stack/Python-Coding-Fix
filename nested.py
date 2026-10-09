"""Select and print employee names for a salary range."""

employees = [
    ["any", 10, 25_000],
    ["ben", 24, 10_000],
    ["chad", 15, 70_000],
]

# Print uppercase names only when salary is > 10,000 and < 40,000.
for employee in employees:
    name, _age, salary = employee
    if 10_000 < salary < 40_000:
        print(name.upper())
