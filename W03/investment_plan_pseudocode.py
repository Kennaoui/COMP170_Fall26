# COMP 170 Standard Python Header
# Assignment: Investment Plan
# Name and Loyola Id/email: xxxxxxx
# Date: September 11, 2026
#
# DESCRIPTION: This program collects information about an investment plan,
# calculates its future value, and displays the results.
#
# QUESTIONS: None
#
# PROBLEM ANALYSIS & KEY ISSUES:
# The program needs to collect information about an investment plan,
# calculate its future value, and display the complete plan.
#
# PROGRAM PSEUDOCODE:
# Call the main function.
# In main:
#     Display one complete investment plan.
#     Test the future-value calculation using different argument combinations.
# To display an investment plan:
#     Read the plan information from the user.
#     Calculate the future value.
#     Display the plan information and the calculated result.
#
# FUNCTIONS:
# read_plan_plan collects the investment information from the user.
# calculate_future_future_value calculates the value of the investment.
# display_plan_plan displays the plan information and calculated value.
# show_plan coordinates the previous three functions.

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
