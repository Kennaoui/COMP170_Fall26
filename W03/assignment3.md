# COMP 170 — Week 3 Assignment

For Exercises 1–3, complete the required pseudocode before writing the Python implementation. Follow the course [pseudocode instructions](https://github.com/Kennaoui/COMP170_Fall26/blob/main/Pseudocode/instructions.md) and [pseudocode template](https://github.com/Kennaoui/COMP170_Fall26/blob/main/Pseudocode/template.py). Include type annotations and docstrings, and use a `main()` function to coordinate each program.

Use only the concepts covered during Weeks 1–3.

## Exercise 1 — Two-Day Temperature Report

Create a file named `temperature_report.py`.

### Part 1 — Conversion Functions

The formula for converting Celsius to Fahrenheit is:

```text
F = C × 9/5 + 32
```

1. Write a function that receives a temperature in Celsius and returns the corresponding temperature in Fahrenheit.

2. Derive the formula for converting Fahrenheit to Celsius from the formula above. Include your algebraic steps as comments, then write a function that receives a temperature in Fahrenheit and returns the corresponding temperature in Celsius.

### Part 2 — Complete Program

Write a `main()` function that prompts the user twice: first for the temperature on Day 1 in Celsius (for example, `20`), and then for the temperature on Day 2 in Fahrenheit (for example, `77`). It should then display output similar to:

```text
Day 1: 20.0 degrees Celsius, or 68.0 degrees Fahrenheit.
Day 2: 77.0 degrees Fahrenheit, or 25.0 degrees Celsius.
Two-day average: 22.5 degrees Celsius, or 72.5 degrees Fahrenheit.
```

Call `main()` at the end of the program.

## Exercise 2 — The House That Jack Built

Create a file named `jack_poem.py`.

Write pseudocode and a Python program that displays the following verses exactly as shown. Use functions and variables to avoid repeating the same instructions or text unnecessarily. Your decomposition should demonstrate that functions can call other functions.

```text
The verses for "Jack" poem

This is the house that Jack built.

This is the malt
That lay in the house that Jack built.

This is the rat,
That ate the malt
That lay in the house that Jack built.

This is the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.

This is the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.

This is the cow with the crumpled horn,
That tossed the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.

This is the maiden all forlorn
That milked the cow with the crumpled horn,
That tossed the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.
```

Call `main()` at the end of the program.

## Exercise 3 — Road-Trip Cost Estimator

Create a file named `road_trip.py`.

Write pseudocode and a Python program that estimates the fuel needed and fuel cost for a road trip. Use a default fuel efficiency of `25` miles per gallon and a default gas price of `$3.50` per gallon.

The program should prompt the user for the trip distance, their vehicle’s fuel efficiency, and the current gas price. It should then produce two estimates: a standard estimate using the default values and a personalized estimate using the values entered by the user.

Example:

```text
Trip distance in miles: 300
Your vehicle's miles per gallon: 30
Current gas price per gallon: 4.00

Standard estimate:
Fuel needed: 12.0 gallons
Fuel cost: $42.0

Personalized estimate:
Fuel needed: 10.0 gallons
Fuel cost: $40.0
```

Decompose the work into different functions, with each function responsible for one specific job. Your solution must demonstrate the use of default arguments.

Call `main()` at the end of the program.

## Exercise 4 — Understanding Functions

For each question, predict the result without running the code. Then run it to check your prediction. Explain briefly how parameters, local variables, returned values, or assignment determine the result.

### Question 1 — Following Multiple Returned Values

```python
def transform(x, y, z):
    x = x + 1
    y = y * 2
    z = z - 3
    return y, x, z


x = 2
y = 5
z = 12

z, y, x = transform(x, y, z)
```

What are the values of `x`, `y`, and `z` after the function call? Carefully follow both the order in which the values are returned and the order in which they are assigned.

### Question 2 — Ignoring a Returned Value

```python
def add_five(value: int) -> int:
    value = value + 5
    return value


number = 10
add_five(number)
print(number)
```

What does the program display? Why does `number` keep or change its value?

### Question 3 — Receiving a Returned Value

```python
def add_five(value: int) -> int:
    value = value + 5
    return value


number = 10
number = add_five(number)
print(number)
```

What does the program display? What important difference between this code and Question 2 explains the result?

### Question 4 — Default, Positional, and Keyword Arguments

```python
def calculate_points(
    base_points: int,
    multiplier: int = 2,
    bonus: int = 5
) -> int:
    return base_points * multiplier + bonus


first = calculate_points(10)
second = calculate_points(10, 3)
third = calculate_points(10, bonus=0)
fourth = calculate_points(bonus=4, base_points=10)
```

What are the values of `first`, `second`, `third`, and `fourth`? For each call, identify the value received by `base_points`, `multiplier`, and `bonus`, and explain whether it came from an argument or a default value.

### Question 5 — Local Variables

```python
def calculate_total(price: float, quantity: int) -> float:
    total = price * quantity
    return total


answer = calculate_total(4.0, 3)
print(answer)
print(total)
```

What happens when the final statement is executed? Explain why `answer` can be used outside the function but `total` cannot.

### Question 6 — Functions Calling Functions

```python
def double(number: int) -> int:
    return number * 2


def add_three(number: int) -> int:
    return number + 3


def calculate(number: int) -> int:
    value = double(number)
    return add_three(value)


result = calculate(5)
```

What is the value of `result`? In what order are the functions called, and how does each returned value move from one function to another?

## What to Submit

Submit the following four files through Sakai:

1. `temperature_report.py`
2. `jack_poem.py`
3. `road_trip.py`
4. Your answers to Exercise 4 as one `.pdf`, `.txt`, or `.md` file

The three Python files must include their pseudocode and final implementations. For Exercise 4, include your predictions, the results obtained after running the code, and your explanations.
