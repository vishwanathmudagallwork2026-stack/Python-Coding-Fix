"""Examples of functions with parameters and return values."""


def send_otp(phone_number):
    """Demonstrate the destination for an OTP; this does not send a real OTP."""
    print(f"Demonstration only: an OTP would be sent to {phone_number}.")
    return 1234  # Fixed sample value for learning, not authentication.


def wish(name):
    """Print a birthday wish and return a sample gift."""
    print(f"Happy birthday, {name}!")
    return "ice cake"


def add(a, b):
    """Return the sum of two values."""
    return a + b


def subtract(a, b):
    """Return the difference of two values."""
    return a - b


def multiply(a, b):
    """Return the product of two values."""
    return a * b


def divide(a, b):
    """Return the quotient, raising a clear error for a zero divisor."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    send_otp("+123456790")
    print("Sample gift:", wish("Vishwanath"))
    print("-----------------")
    print(add(10, 20))
    print(subtract(10, 20))
    print(multiply(10, 20))
    print(divide(10, 20))
