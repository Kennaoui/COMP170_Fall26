# Name: xxxx

# Investment PLan Calculator
# This program collects information about an investment plan, 
# calculates its future value, and displays the results.
# 1. Read the information for an investment plan.
# 2. Calculate the future value of the investment.
# 3. Display the plan and its future value.
# 4. Test the calculation using default argument values.


def read_plan() -> tuple[str, float, float, int]: # We will discuss what tuples are later this semester
    """
    Ask the user for the plan name.
    Ask the user for the starting amount.
    Ask the user for the annual interest rate.
    Ask the user for the number of years.
    Return all the entered information.
    """
    name = input("Plan name: ")
    principal = float(input("Starting amount: "))
    rate = float(input("Annual rate as a decimal: "))
    years = int(input("Number of years: "))

    return name, principal, rate, years


def calculate_future_value( principal: float, rate: float = 0.5, years: int = 5) -> float:
    """
    Calculate the future value of the invested principal.
    Takes as input the principal , rate (default 0.5), and years (default 5).
    Return the calculated value.
    """
    return principal * (1 + rate) ** years


def display_plan(
    name: str,
    principal: float,
    rate: float = 0.5,
    years: int = 5,
    future_value: float ) -> None:
    """
    Takes as input the principal , rate (default 0.5), and years (default 5).
    Display the plan name.
    Display the starting amount, rate, and number of years.
    Display the future value rounded to two decimal places.
    """
    print("PLAN:", name)
    print("Deposit:", principal, "Rate:", rate, "Years:", years)
    print("Future value:", round(future_value, 2))


def show_plan() -> None:
    """
    Prompts the user for information for one investment plan by calling read_plan()
    Calculate its future value 
    Display the plan information and calculated value 
    """
    name, principal, rate, years = read_plan()
    value = calculate_future_value(principal, rate, years)
    display_plan(name, principal, rate, years, value)


def main():
    # Test 1: values entered by the user
    show_plan()

    # Test 2: default values
    print(calculate_future_value(1000))
    print(calculate_future_value(1000, 0.5))
    print(calculate_future_value(1000, years=10))


main()
