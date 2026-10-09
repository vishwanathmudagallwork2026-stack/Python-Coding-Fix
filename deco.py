"""Examples of decorators that support both positional and keyword arguments."""

from functools import wraps


def add_box_decoration(function):
    """Print packaging steps before and after the wrapped function runs."""
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("Picks up the ready-made box")
        result = function(*args, **kwargs)
        print("Adds a label to the cake box")
        return result

    return wrapper


@add_box_decoration
def bake_cake(flavour="chocolate", bakery="home"):
    """Describe the cake being prepared."""
    print(f"{flavour} cake chosen from {bakery} bakery")


if __name__ == "__main__":
    bake_cake()
    print("-----------------")
    bake_cake("dark forest", bakery="Iyengar")
