# COMP 170 — Week 4 Assignment: Loops

For Exercises 1–3, write the pseudocode **before** writing the Python implementation. Place the pseudocode in comments at the top of each Python file. It should explain the overall strategy of the program, including what the loop repeats and what values change during the repetition.

Follow the course [pseudocode instructions](https://github.com/Kennaoui/COMP170_Fall26/blob/main/Pseudocode/instructions.md) and [pseudocode template](https://github.com/Kennaoui/COMP170_Fall26/blob/main/Pseudocode/template.py).

For every function:

- Add type annotations for all parameters and return values.
- Add a docstring that clearly explains the function's responsibility.
- Give the function one focused job.

Use a `main()` function to coordinate each program, and call `main()` at the end of the file.

Use only concepts covered during Weeks 1–4. In particular:

- Use `for` loops and `range()` for repetition.
- Do **not** use `if` statements, `while` loops, `break`, or `continue`.
- Do not use lists or other collections to store all the values entered by the user. Process each value as it is entered.

## Exercise 1 — Dinner Receipt

Create a file named `dinner_receipt.py`.

Write a program that creates one receipt for a group dinner. The program should first ask how many people ate. It should then prompt for the cost of each person's dinner and use a loop to calculate the subtotal.

After all dinner costs have been entered, calculate and display:

- the subtotal;
- an 8% tax;
- a 15% tip, calculated from the subtotal before tax; and
- the final total.

Declare the tax rate and tip rate as constants near the top of the file.

Example interaction:

```text
How many people ate? 4
Person #1: How much did your dinner cost? 20.00
Person #2: How much did your dinner cost? 15
Person #3: How much did your dinner cost? 30.0
Person #4: How much did your dinner cost? 10.00

Subtotal: $75.0
Tax: $6.0
Tip: $11.25
Total: $92.25
```

Structure the program using the following three functions:

1. `calculate_subtotal()` — receives the number of people, repeatedly prompts for each person's dinner cost, and returns the subtotal.
2. `display_receipt()` — receives the subtotal, calculates the tax, tip, and total, and displays the completed receipt.
3. `main()` — prompts for the number of people and coordinates the program by calling the other functions.

## Exercise 2 — Framed Hourglass

Create a file named `framed_hourglass.py`.

### Part 1 — Fixed-Size Hourglass

First, write a function that displays the following hourglass of size `4` exactly as shown. Use loops to produce the changing spaces and stars. Do not use a separate `print()` statement for every line.

```text
+---------+
|\*******/|
| \*****/ |
|  \***/  |
|   \*/   |
|   /*\   |
|  /***\  |
| /*****\ |
|/*******\|
+---------+
```

### Part 2 — Resizable Hourglass

Next, generalize the program so that it prompts the user for a size and displays an hourglass following the same pattern.

For example, an hourglass of size `3` should be:

```text
+-------+
|\*****/|
| \***/ |
|  \*/  |
|  /*\  |
| /***\ |
|/*****\|
+-------+
```

An hourglass of size `2` should be:

```text
+-----+
|\***/|
| \*/ |
| /*\ |
|/***\|
+-----+
```

The number of stars changes by `2` from one line to the next. Use the `step` argument of `range()` to produce this change; do not generate the odd numbers using a separate counter.

Decompose the resizable solution into the following functions:

1. `display_border()` — receives the size and displays one horizontal border.
2. `display_upper_half()` — receives the size and displays the shrinking upper half, using `\` on the left and `/` on the right.
3. `display_lower_half()` — receives the size and displays the expanding lower half, using `/` on the left and `\` on the right.
4. `display_hourglass()` — receives the size and assembles the complete figure by calling the other display functions.
5. `main()` — prompts for the size and coordinates the program.

The fixed-size and resizable versions must both appear in your submitted file. Add a brief comment identifying each part.

## Exercise 3 — Number Triangle

Create a file named `number_triangle.py`.

Study the following output carefully and determine how the values in each row are generated.

For a size of `5`, the program should display:

```text
1
2 6
3 9 15
4 12 20 28
5 15 25 35 45
```

For a size of `7`, it should display:

```text
1
2 6
3 9 15
4 12 20 28
5 15 25 35 45
6 18 30 42 54 66
7 21 35 49 63 77 91
```

Write a program that prompts the user for the size and displays the corresponding number triangle. Your solution must use nested loops and must work for sizes other than the two examples above.

Generate the needed sequence directly through `range()` with *step = 2*.

Do not write a separate `print()` statement for each row or hard-code the displayed values. Part of the exercise is determining how to calculate each value from its row and its position in the triangle. Explain the rule you identified in your pseudocode.

Your program must include:

1. `display_number_row()` — receives the information needed to display one complete row and uses a loop to produce its values on the same line.
2. `display_number_triangle()` — receives the size, uses a loop to produce all rows, and calls `display_number_row()` during each iteration.
3. `main()` — prompts for the size and coordinates the program.

## What to Submit

Submit the following three files through Sakai:

1. `dinner_receipt.py`
2. `framed_hourglass.py`
3. `number_triangle.py`

Each file must include:

- pseudocode at the top of the file;
- the complete Python implementation;
- all required functions;
- type annotations and docstrings for every function; and
- a call to `main()` at the end.

Before submitting, run each program more than once using different input values. Make sure the number of loop iterations changes correctly when the user enters a different number of people, hourglass size, or triangle size.
