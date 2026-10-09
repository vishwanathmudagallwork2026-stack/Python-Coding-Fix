"""Examples of nested functions, enclosing variables, and nonlocal."""

# An inner function can be defined and called inside an outer function.
def outer():
    def inner():
        print("Inside the inner function")

    print("Inside the outer function")
    inner()


outer()

# Variables in an enclosing function can be read by an inner function.
global_value = 100


def show_values():
    local_value = 20

    def show_inner_values():
        print("Global:", global_value, "Enclosing:", local_value)

    show_inner_values()


show_values()

# `nonlocal` allows the inner function to modify the enclosing variable.
def make_counter():
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
