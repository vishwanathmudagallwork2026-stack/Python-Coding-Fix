"""Print even values from a list using an index-controlled while loop."""

numbers = [11, 12, 15, 24, 37, 40]
index = 0

while index < len(numbers):
    if numbers[index] % 2 == 0:
        print(numbers[index])
    index += 1
