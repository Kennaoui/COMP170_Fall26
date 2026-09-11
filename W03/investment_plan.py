
def show_plan(plan_name, principal, rate, years):
    value = principal * (1 + rate) ** years
    print("PLAN:", plan_name)
    print("Deposit:", principal, "Rate:", rate, "Years:", years)
    print("Future value:", round(value, 2))


show_plan("Starter", 1000, 0.03, 5)
show_plan("Growth", 1500, 0.04, 8)
show_plan("Long-Term", 2000, 0.05, 10)
     
