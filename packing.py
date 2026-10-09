"""Examples of tuple packing and iterable unpacking."""

# Packing: multiple values form a tuple.
person_names = ("ram", "sham", "hari")
print(type(person_names))

# Unpack exactly four values into four variables.
numbers = [10, 20, 30, 40]
a, b, c, d = numbers
print(a)
print(b)
print(c)
print(d)

# Extended unpacking stores the remaining values in a list.
values = [1, 23, 5, 67, 89, 0, 5, 4, 5, 99]
first, second, third, *remaining = values
print(first)
print(second)
print(third)
print(remaining)

print("-----------------")

# The starred variable can also appear in the middle of unpacking.
characters = "RCSKB"
first_character, *middle_characters, last_character = characters
print(first_character)
print(middle_characters)
print(last_character)
