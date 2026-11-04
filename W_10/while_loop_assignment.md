# COMP 170 – Week 10: While Loops

## Rules

- **Submit:** `ex1_answers.pdf`, `electric_car.py`, `car_main.py`, `collatz.py`.
- Every function and method needs a **docstring**.
- **Not allowed:** `break`, `continue`, `while True:`.
- You can assume the user types a number when the program asks for one.

---

## Exercise 1: How while loops work

Write your answers in `ex1_answers.pdf`.

### (a) The three questions

For the loop below, answer these questions:

1. What is set up before the loop?
2. What condition keeps the loop going?
3. What changes inside the loop so that it stops?

Also say how many times the body runs.

```python
balance = 100.0
years = 0
while balance < 150.0:
    balance = balance * 1.10
    years = years + 1
print(years)
```

### (b) Trace

Trace the code for `n = 4072`. Make a table showing `n`, `digits` and `total` after each pass, then give the output.

```python
n = 4072
digits = 0
total = 0
while n > 0:
    total = total + n % 10
    n = n // 10
    digits = digits + 1
print(digits, total)
```

1. What does this code compute?
2. What does it print for `n = 0`? How many times does the body run?

### (c) Sentinel loop

Trace the code with the inputs `72`, `95`, `88`, `-1`.

```python
count = 0
largest = 0
score = int(input("Score (-1 to stop): "))
while score != -1:
    count = count + 1
    if score > largest:
        largest = score
    score = int(input("Score (-1 to stop): "))
print(count, largest)
```

1. What does it print? What does it print if the first input is `-1`?
2. Why is there one `input` before the loop and another at the end of the body?
3. Why is `-1` a good sentinel here? Pick a sentinel for:
   - ages
   - temperatures in °C
   - student names

### (d) Find and fix the bug

For each snippet:

- say what happens with the given input,
- explain why,
- fix it.

**A.** Countdown.

```python
i = 10
while i > 0:
    print(i)
print("Liftoff!")
```

**B.** Average of prices. Input: `4.0`, `6.0`, `0`. The expected output is `Average: 5.0`.

```python
total = 0.0
count = 0
price = 1.0
while price != 0:
    price = float(input("Price (0 to stop): "))
    total = total + price
    count = count + 1
print("Average:", total / count)
```

**C.** Age from 0 to 120. Input: `-5`, `200`, `19`.

```python
age = int(input("Age (0-120): "))
if age < 0 or age > 120:
    print("Out of range, try again.")
    age = int(input("Age (0-120): "))
print("Your age is", age)
```

**D.** Yes/no question. Input: `y`.

```python
answer = input("Continue? (y/n): ")
while answer != "y" or answer != "n":
    print("Please type y or n.")
    answer = input("Continue? (y/n): ")
```

### (e) Fencepost

This code prints `1, 2, 3, 4, 5, ` with an extra comma at the end.

```python
n = 5
i = 1
while i <= n:
    print(i, end=", ")
    i = i + 1
```

1. Why is this a *fencepost* problem?
2. Fix the code so it prints `1, 2, 3, 4, 5`. Don't put an `if` inside the loop. It must also work for `n = 1`.
3. What does your version print for `n = 0`? Is that OK?

### (f) For or while?

1. Choose `for` or `while` for each task, and give one sentence of explanation:
   1. Print each character of a word.
   2. Ask for a password until it is correct.
   3. Add the numbers from 1 to 100.
   4. Double a number until it is larger than 1000, and count the doublings.
   5. Read scores until the user types `-1`.
   6. Print 7 × 1 through 7 × 10.
2. Rewrite this loop as a `while` loop:

   ```python
   for i in range(3, 20, 4):
       print(i)
   ```

3. In one or two sentences: when do you use `for`, and when do you use `while`?

---

## Exercise 2: ElectricCar

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

## Exercise 3: The 3n+1 sequence

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
# COMP 170 – Week 10: While Loops

## Rules

- **Submit:** `ex1_answers.pdf`, `electric_car.py`, `car_main.py`, `collatz.py`.
- Every function and method needs a **docstring**.
- **Not allowed:** `break`, `continue`, `while True:`.
- You can assume the user types a number when the program asks for one.

---

## Exercise 1: How while loops work

Write your answers in `ex1_answers.pdf`.

### (a) The three questions

For the loop below, answer these questions:

1. What is set up before the loop?
2. What condition keeps the loop going?
3. What changes inside the loop so that it stops?

Also say how many times the body runs.

```python
balance = 100.0
years = 0
while balance < 150.0:
    balance = balance * 1.10
    years = years + 1
print(years)
```

### (b) Trace

Trace the code for `n = 4072`. Make a table showing `n`, `digits` and `total` after each pass, then give the output.

```python
n = 4072
digits = 0
total = 0
while n > 0:
    total = total + n % 10
    n = n // 10
    digits = digits + 1
print(digits, total)
```

1. What does this code compute?
2. What does it print for `n = 0`? How many times does the body run?

### (c) Sentinel loop

Trace the code with the inputs `72`, `95`, `88`, `-1`.

```python
count = 0
largest = 0
score = int(input("Score (-1 to stop): "))
while score != -1:
    count = count + 1
    if score > largest:
        largest = score
    score = int(input("Score (-1 to stop): "))
print(count, largest)
```

1. What does it print? What does it print if the first input is `-1`?
2. Why is there one `input` before the loop and another at the end of the body?
3. Why is `-1` a good sentinel here? Pick a sentinel for:
   - ages
   - temperatures in °C
   - student names

### (d) Find and fix the bug

For each snippet:

- say what happens with the given input,
- explain why,
- fix it.

**A.** Countdown.

```python
i = 10
while i > 0:
    print(i)
print("Liftoff!")
```

**B.** Average of prices. Input: `4.0`, `6.0`, `0`. The expected output is `Average: 5.0`.

```python
total = 0.0
count = 0
price = 1.0
while price != 0:
    price = float(input("Price (0 to stop): "))
    total = total + price
    count = count + 1
print("Average:", total / count)
```

**C.** Age from 0 to 120. Input: `-5`, `200`, `19`.

```python
age = int(input("Age (0-120): "))
if age < 0 or age > 120:
    print("Out of range, try again.")
    age = int(input("Age (0-120): "))
print("Your age is", age)
```

**D.** Yes/no question. Input: `y`.

```python
answer = input("Continue? (y/n): ")
while answer != "y" or answer != "n":
    print("Please type y or n.")
    answer = input("Continue? (y/n): ")
```

### (e) Fencepost

This code prints `1, 2, 3, 4, 5, ` with an extra comma at the end.

```python
n = 5
i = 1
while i <= n:
    print(i, end=", ")
    i = i + 1
```

1. Why is this a *fencepost* problem?
2. Fix the code so it prints `1, 2, 3, 4, 5`. Don't put an `if` inside the loop. It must also work for `n = 1`.
3. What does your version print for `n = 0`? Is that OK?

### (f) For or while?

1. Choose `for` or `while` for each task, and give one sentence of explanation:
   1. Print each character of a word.
   2. Ask for a password until it is correct.
   3. Add the numbers from 1 to 100.
   4. Double a number until it is larger than 1000, and count the doublings.
   5. Read scores until the user types `-1`.
   6. Print 7 × 1 through 7 × 10.
2. Rewrite this loop as a `while` loop:

   ```python
   for i in range(3, 20, 4):
       print(i)
   ```

3. In one or two sentences: when do you use `for`, and when do you use `while`?

---

## Exercise 2: ElectricCar

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

## Exercise 3: The 3n+1 sequence

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
