"""Convert strings into numeric and boolean values safely."""

# Convert strings to numeric types.
integer_value = int("10")
float_value = float("13.4")
print(integer_value)
print(float_value)

# bool("False") is True because every non-empty string is truthy.
# Parse textual booleans explicitly instead of using bool() or eval().
boolean_text = "False"
boolean_value = boolean_text.strip().lower() in {"true", "yes", "1"}
print(boolean_value)
