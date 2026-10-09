"""Examples of for loops, while loops, totals, and student grades."""

# Repeat a message 30 times.
for _ in range(30):
    print("Good morning, students")

# Print a sequence of integers.
for number in range(5):
    print(number)

fruits = ["apple", "banana", "grapes"]
for fruit in fruits:
    print(fruit)

# Iterate over a string one character at a time.
for character in "python":
    print(character)

# Sum integers from 0 through 8.
total = sum(range(9))
print("Total sum:", total)

prices = [100, 200, 300, 400, 500]
print("Total price:", sum(prices))

# Store each student as (name, marks), then print a report.
students = [("Alice", 92), ("Bob", 78), ("Charlie", 85), ("Diana", 60), ("Eve", 45)]
total_marks = 0
for name, marks in students:
    total_marks += marks
    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    elif marks >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"Name: {name}, Marks: {marks}, Grade: {grade}")

# Calculate the average from the actual number of students.
if students:
    print(f"\nClass average: {total_marks / len(students):.2f}")

count = 0
while count < 3:
    print("Count is:", count)
    count += 1

# Add successive positive integers until the total becomes greater than 20.
total = 0
number = 1
while total <= 20:
    total += number
    print(f"Added {number}; total is now {total}")
    number += 1
