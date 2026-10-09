"""Print a calendar month for a user-supplied year and month."""

import calendar


def main():
    """Validate input and print the requested calendar month."""
    try:
        year = int(input("Enter the year: "))
        month = int(input("Enter the month (1-12): "))
        if year < 1 or not 1 <= month <= 12:
            raise ValueError
    except ValueError:
        print("Please enter a positive year and a month from 1 to 12.")
        return

    print(calendar.month(year, month))


if __name__ == "__main__":
    main()
