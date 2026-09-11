def read_plan():
    name = input("Plan name: ")
    principal = float(input("Starting amount: "))
    rate = float(input("Annual rate as a decimal: "))
    years = int(input("Number of years: "))
    return name, principal, rate, years


def calculate_future_value(principal, rate = 0.5, years = 5):
    return principal * (1 + rate) ** years


def display_plan(name, principal, rate, years, future_value):
    print("PLAN:", name)
    print("Deposit:", principal, "Rate:", rate, "Years:", years)
    print("Future value:", round(future_value, 2))

def show_plan():
    name, principal, rate, years = read_plan()
    value = calculate_future_value(principal, rate, years)
    display_plan(name, principal, rate, years, value)
    
def main(): 
    #Test 1
    show_plan()
    #Test 2 (with default values)
    print(calculate_future_value(1000))
    print(calculate_future_value(1000, 0.5))
    print(calculate_future_value(1000, years = 10))
main()
