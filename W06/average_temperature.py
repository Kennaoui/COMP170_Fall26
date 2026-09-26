def average_temperature() -> float:
    """Read each day's high temp; print and return the average."""

    days = int(input("How many days' temperatures? "))

    total = 0  # accumulator

    for i in range(days):
        prompt = "Day " + str(i + 1) + "'s high temp: "
        temp = int(input(prompt))
        total += temp  # running total

    average = total / days

    print("Average temp =", round(average, 1))

    return average
