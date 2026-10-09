"""A closure-based counter and a basic function decorator."""

from functools import wraps


def make_counter():
    """Create a counter whose state is preserved between calls."""
    count = 0

    def increment():
        nonlocal count
        count += 1
        print(count)
        return count

    return increment


counter = make_counter()
counter()
counter()
counter()


def add_preparation_steps(function):
    """Print preparation steps before running the decorated function."""
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("Preparing the cake box")
        result = function(*args, **kwargs)
        print("Adding a label to the cake box")
        return result

    return wrapper


@add_preparation_steps
def bake_cake(flavour):
    """Describe the cake selected by the user."""
    print(f"{flavour} cake chosen")


bake_cake("chocolate")
