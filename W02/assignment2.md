# COMP 170 — Week 2 Exercises

### Expressions, Variables, Operators, `input()`, and Errors

---

What to submit: Submit five Python files, named `exercise1.py` through `exercise5.py`. Each file must run independently. Include all requested written answers as comments in the corresponding file.

---

## Exercise 1 — Receipt Header

Write a program that prints exactly the following four lines. Use one `print()` statement per line.

```text
"Fresh Mart" - Thanks for shopping!
Cashier said: "Have a great day!"
Today's special: Maria's Bakery Bread
He whispered, "It's closing time."
```

---

## Exercise 2 — Study Session Snacks

Write a program that checks whether a study group’s snack order is a good deal.

Prompt the user for:

* the price of one snack box
* the number of boxes ordered
* the number of people in the group
* the number of snacks in each box
* the maximum acceptable price per person

You may assume that all inputs are positive and that there are at least as many snacks as people.

Calculate and print:

1. The total number of snacks.
2. The number of snacks each person receives and the number left over when the snacks are divided evenly.
3. The total cost of the order.
4. The effective cost of each distributed snack. First divide the total cost by the number of people, and then divide that result by the number of snacks each person receives. Ignore leftover snacks in this calculation.
5. A `True` or `False` value indicating whether the order is within budget. Compare the cost per person directly with the maximum acceptable price per person.

### Reflection

Answer these questions as comments in `exercise2.py`:

1. Calculate `2 ** 3 ** 2` and `20 - 5 - 3` by hand, and then check your answers in Python. What do the results show about the direction in which `**` and `-` are evaluated?
2. Predict the value of `-7 % 3`, and then check it in Python. Were you correct? What did you learn about `%` with negative numbers?
3. Is the number of snacks each person receives an `int` or a `float`? What error would occur if you forgot to convert the value returned by `input()` for the number of people to an integer?

---

## Exercise 3 — Find the Bugs

The following program is supposed to calculate the total price of a coffee order after applying a percentage discount. It contains exactly three mistakes:

* one syntax error
* one runtime error
* one logic error

```python
price_per_cup = float(input("Price per cup: "))
num_cups = int(input("How many cups: "))
discount_percent = int(input("Discount percent (0 if none): "))

subtotal = price_per_cup * num_cup
total = subtotal - discount_percent

print("Subtotal: $" + str(subtotal)
print("Total after discount: $" + str(total))
```

Find and fix all three mistakes. For each mistake, add a comment identifying whether it is a syntax, runtime, or logic error.

With a price of `4.50`, `3` cups, and a `10` percent discount, the corrected program should print:

```text
Subtotal: $13.5
Total after discount: $12.15
```

---

## Exercise 4 — Discover Compound Assignment

The operators `+=`, `-=`, and `*=` have not yet been covered in class. In this exercise, you will determine what they do and then use them in a program.

### Step 1 — Experiment

Predict the output of each block before running it:

```python
x = 5
x += 3
print(x)

y = 10
y -= 4
print(y)

z = 2
z *= 5
print(z)
```

As comments in `exercise4.py`, explain in one sentence what each operator does. Also give the ordinary assignment statement for which it is shorthand. For example:

```python
x += 3  # Shorthand for x = = ______
```

### Step 2 — Apply

Use compound assignment to track a trivia team’s score:

* Start the score at `0`.
* Round 1: add 10 points.
* Round 2: subtract 4 points.
* Round 3: double the current score.

Use one compound assignment operator in each round. Do not use statements such as `score = score + 10`.

Print the score after each round with a clear label.

---

## Exercise 5 — Tab Hexagon

For this exercise, assume that tab stops occur every eight columns. A tab character, `\t`, moves the cursor to the next tab stop. A newline character, `\n`, begins a new line.

For example:

* From column 3, `\t` moves to column 8.
* From column 8, `\t` moves to column 16.
* In general, a tab adds `8 - (column % 8)` spaces.

Using one `print()` statement and one string containing `\t` and `\n`, display this hexagon:

```text
                *
        *               *
*                               *
*                               *
        *               *
                *
```

Do not include literal space characters inside the string. All horizontal spacing must be created using `\t`.
