def print_report(temps: list[float]) -> None:
    """Print each temperature, numbered from day 1."""
    day = 1
    for temp in temps:
        print("Day", day, ":", temp)
        day += 1


def to_celsius(temps: list[float]) -> None:
    """Convert every temperature from F to C, in place."""
    for i in range(len(temps)):
        temps[i] = round((temps[i] - 32) * 5 / 9, 1)


week = [50.0, 68.0, 32.0]
to_celsius(week)  # returns None; changes week
print(week)       # [10.0, 20.0, 0.0]
