"""Examples of string indexing, slicing, methods, and membership."""

name = "vishwanath"

# Indexing uses zero-based positions; negative indexes count from the end.
print(name[0])   # v
print(name[-9])  # i

# The stop index is excluded from a slice.
print(name[0:4])  # vish
print(name[4:7])  # wan
print(name[-1])   # h
print(name[:2])   # vi
print(name[2:5])  # shw

# String methods return new strings; they do not modify the original string.
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())
print(name.replace("vishwanath", "VISHWANATH"))
print(name.strip())
print(name.count("a"))  # 2
print(name.find("h"))   # 3 (the first occurrence)
print(name.split("a"))  # ['vishw', 'n', 'th']
print(name.startswith("v"))
print(name.endswith("h"))

# Membership checks whether a substring occurs in a string.
email = "vishwanath@example.com"
print("@" in email)
print(".com" in email)
print("google" in email)
print("gmail" in email)

# Repetition and concatenation.
print("Ha" * 3)
first_name = "Vishwanath"
last_name = "Mudagall"
full_name = f"{first_name} {last_name}"
print(full_name)

# Small practice exercise.
name = "Vishwanath"
print(name.upper())
print(name.lower())
print(name[:4])
print(len(name))
print(name[::-1])
print("anath" in name)
