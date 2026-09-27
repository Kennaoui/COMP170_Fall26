from list_toolbox import list_average, count_above


def read_temps(days: int) -> list[int]:
    """Ask for one high temp per day; return them as a list."""
    temps = []
    for i in range(days):
        prompt = "Day " + str(i + 1) + "'s high temp: "
        temps.append(int(input(prompt)))
    return temps


def main() -> None:
    """Run the weather report."""
    days = int(input("How many days' temperatures? "))
    temps = read_temps(days)  # input
    avg = list_average(temps)  # compute
    print("Average temp =", round(avg, 1))  # output
    print(count_above(temps, avg), "days were above average.")


main()
