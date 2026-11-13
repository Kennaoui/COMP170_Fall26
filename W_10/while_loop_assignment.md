# COMP 170 – Assignment 9: While Loops

## Rules

- **Submit:** `electric_car.py`, `car_main.py`, `collatz.py`.
- Every function and method needs a **docstring**.
- **Not allowed:** `break`, `continue`, `while True:`.
- You can assume the user types a number when the program asks for one.

---

## Exercise 1: ElectricCar

Put this class in `electric_car.py`. `__capacity` and `__charge` are **private**.

```python
class ElectricCar:
    """An electric car with a nickname, a battery, and an efficiency."""

    def __init__(self, nickname, capacity, km_per_kwh):
        """Create a car with a full battery. capacity is in kWh;
        km_per_kwh is how many km the car drives on 1 kWh."""
        self.nickname = nickname
        self.__capacity = capacity      # private
        self.__charge = capacity        # private
        self.km_per_kwh = km_per_kwh

    def get_nickname(self):
        """Return the car's nickname."""
        return self.nickname

    def get_capacity(self):
        """Return the battery's capacity, in kWh."""
        return self.__capacity

    def get_charge(self):
        """Return the energy left in the battery, in kWh."""
        return self.__charge

    def get_range(self):
        """Return how many km the car can drive on its current charge."""
        return self.__charge * self.km_per_kwh

    def drive(self, km):
        """Drive km if there is enough charge and use up the energy.
        Return True if the drive happened, False otherwise."""
        needed = km / self.km_per_kwh
        driven = False
        if needed <= self.__charge:
            self.__charge = self.__charge - needed
            driven = True
        return driven

    def __str__(self):
        """Return a string like 'Sparky: 42.5/60.0 kWh'."""
        return (self.nickname + ": " + format(self.__charge, ".1f") + "/"
                + format(self.__capacity, ".1f") + " kWh")
```

### (a) Add `minutes_to_charge(target)`

Return the number of minutes needed for the charge to reach at least `target` kWh. Simulate one minute at a time:

- Below 80% of capacity, each minute adds **1.0 kWh**.
- From 80% up, each minute adds **0.25 kWh**.
- The charge never goes above the capacity.

The method must **not** change `__charge`. If the charge is already at least `target`, return `0`.

In the docstring, state the preconditions and postconditions.

```text
sparky = ElectricCar("Sparky", 60.0, 6.0)
sparky.drive(240.0)                 # 20 kWh left
sparky.minutes_to_charge(48.0)   ->  28
sparky.minutes_to_charge(54.0)   ->  52
sparky.minutes_to_charge(60.0)   ->  76
sparky.minutes_to_charge(10.0)   ->  0
sparky.get_charge()              ->  20.0   (unchanged)
```

Answer these in a comment:

1. Why use a while loop here instead of one division?
2. What happens with `target = 70.0` on this car?
3. Why is it a good idea that there is no `set_charge` method?

### (b) Write `car_main.py`

1. Create two cars:
   - `Sparky`: 60.0 kWh, 6.0 km per kWh
   - `Zip`: 40.0 kWh, 7.0 km per kWh
2. **Driving loop.** Ask `Car (1 = Sparky, 2 = Zip, 0 = done):`.
   - `0` stops the loop (sentinel).
   - Any other value except 1 or 2: ask again (retry).
3. For the chosen car:
   - Ask for a distance, which must be > 0 (retry).
   - If the car can't make the trip, print `Not enough charge.` and its range.
   - Print the car.
4. After the loop, print the number of trips and both cars.
5. **Charging plan.** For each car:
   - Ask for a target, which must be > 0 and ≤ capacity (retry).
   - Print the minutes it takes, using `minutes_to_charge`.

More rules:

- Don't copy the same retry loop in several places.
- Use only the getters. Never use `car.__charge` or `car.__capacity` directly.

**Sample run:**

```text
Car (1 = Sparky, 2 = Zip, 0 = done): 1
Distance in km: 150
Sparky: 35.0/60.0 kWh
Car (1 = Sparky, 2 = Zip, 0 = done): 3
Please enter 0, 1, or 2.
Car (1 = Sparky, 2 = Zip, 0 = done): 2
Distance in km: 400
Not enough charge. Range is 280.0 km.
Zip: 40.0/40.0 kWh
Car (1 = Sparky, 2 = Zip, 0 = done): 2
Distance in km: -20
Please enter a number greater than 0.
Distance in km: 70
Zip: 30.0/40.0 kWh
Car (1 = Sparky, 2 = Zip, 0 = done): 0

Trips attempted: 3
Sparky: 35.0/60.0 kWh
Zip: 30.0/40.0 kWh

Charging plan for Sparky
  Target charge in kWh: 55
  Sparky reaches 55.0 kWh in 41 minutes.
Charging plan for Zip
  Target charge in kWh: 65
Target must be more than 0 and at most 40.0.
  Target charge in kWh: 40
  Zip reaches 40.0 kWh in 34 minutes.
```

---

## Exercise 2: The 3n+1 sequence

Start with a whole number n ≥ 1:

- If n is even, the next number is n / 2.
- If n is odd, the next number is 3n + 1.
- Stop at 1.

For example, starting at 6: 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1. That is 8 steps, and the highest value is 16.

**Write `collatz.py` that:**

1. Asks for a starting number ≥ 1 and asks again if the input is invalid.
2. Prints the sequence with ` -> ` between numbers and no extra arrow.
3. Prints the number of steps and the highest value.
4. Asks `Try another number? (y/n):`. Ask again for anything other than `y` or `n`.
5. At the end, prints how many numbers were tried and which one took the most steps.

**Submit:**

- **Pseudocode first**, as comments at the top of the file. Include the problem analysis and the plan for each function.
- Your code. Each function does one job: read, calculate, or display.
- A docstring for every function.

**Sample run:**

```text
Starting number (1 or more): 0
The number must be at least 1.
Starting number (1 or more): 6
6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
Steps: 8
Highest value: 16
Try another number? (y/n): yes
Please type y or n.
Try another number? (y/n): y
Starting number (1 or more): 1
1
Steps: 0
Highest value: 1
Try another number? (y/n): n
You tried 2 numbers.
Longest: 6 with 8 steps.
```
Also test 27 (111 steps, highest value 9232).
