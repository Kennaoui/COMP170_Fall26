def calculate_future_value(principal, rate, years):
    value = principal * (1 + rate) ** years
    return value
    
def display_plan(plan_name, principal, rate, years, value):
    print("PLAN:", plan_name)
    print("Deposit:", principal, "Rate:", rate, "Years:", years)
    print("Future value:", round(value, 2))


value1 = calculate_future_value(1000, 0.03, 5)
display_plan("Starter", 1000, 0.03, 5, value1)

value2 = calculate_future_value(1500, 0.04, 8)
display_plan("Growth", 1500, 0.04, 8, value2)

value3 = calculate_future_value( 2000, 0.05, 10)
display_plan("Long-Term", 2000, 0.05, 10, value3)
     
