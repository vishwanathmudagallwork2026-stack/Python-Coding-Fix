"""Demonstrate a closure: the inner function retains an outer variable."""


def make_greeter(colour="Blue"):
    """Return a function that remembers the selected colour."""
    def greet():
        print(f"The selected colour is {colour}.")

    return greet


say_colour = make_greeter()
say_colour()

say_red = make_greeter("Red")
say_red()
