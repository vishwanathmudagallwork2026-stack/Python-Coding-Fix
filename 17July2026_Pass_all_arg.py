"""Demonstrate positional, variadic, keyword-only, and keyword arguments."""


def order(customer_name, host_name, *starters, drinks="water", **mains):
    """Print an order; *starters gathers extras and **mains gathers named dishes."""
    print("Customer:", customer_name)
    print("Host:", host_name)
    print("Starters:", starters)
    print("Drink:", drinks)
    print("Main dishes:", mains)


order("Boss", "Vishu", "soup", "salad", drinks="lemon water", curry="paneer")
