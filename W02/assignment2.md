# COMP 170 — Week 2 Exercises
### Expressions, Variables, Operators, input() and Errors
---
**What to submit:** one `.py` file per exercise (five files total, named `exercise1.py` through `exercise5.py`), each runnable on its own. Include your written answers to the Reflection questions as comments at the top of the exercise's file.
---

## Exercise 1 — Study Session Snacks

Write a single program that checks whether a study group's snack order is actually a good deal.

**Prompt for:**
- the price of one snack box
- how many boxes were ordered
- how many people are in the group
- how many snacks come in one box
- the maximum price per person the group agreed was acceptable

**Calculate and print:**
1. The total number of snacks ordered.
2. How many snacks each person gets, and how many are left over, if split evenly.
3. The total cost of the order.
4. The cost per person, *per snack* — the total cost divided by the number of people, divided by how many snacks each person got. Match that grouping exactly: adding a parenthesis in the wrong place gives a different number, and Python won't warn you when it happens.
5. A `True`/`False` value for whether the order is within budget: compare the cost per person (total cost ÷ number of people) directly to `max_price_per_person`. 

**Reflection (short answer):**
- By hand, work out `2 ** 3 ** 2` and `20 - 5 - 3`. What does that tell you about which direction `**` evaluates in, compared to `-`?
- Predict what `-7 % 3` evaluates to before you run it. Were you right? What does that tell you about how Python's `%` behaves, compared to how you'd find a remainder by hand?
- Is the "snacks each person gets" value from step 2 an `int` or a `float`? What would change about it if you'd forgotten to convert `num_people` with `int()`?

---

## Exercise 2 — Receipt Header

A quick one: write a program that prints **exactly** the following four lines (using one `print()` per line — four total):

```
"Fresh Mart" - Thanks for shopping!
Cashier said: "Have a great day!"
Today's special: Maria's Bakery Bread
He whispered, "It's closing time."
```

---

## Exercise 3 — Tab Hexagon

**How `\t` actually works:** a tab does *not* insert a fixed number of spaces. It moves the cursor forward to the next column that's a multiple of 8, counting from the start of the current line (column 0 is where the line begins). So the number of spaces it adds depends entirely on where the cursor already is:
- Cursor at column 3 → `\t` adds **5** spaces (to reach column 8).
- Cursor at column 8 (already a multiple of 8) → `\t` still adds a **full 8** spaces, landing on column 16. A tab always moves forward — it never adds zero spaces.
- General rule: it adds `8 - (column % 8)` spaces — which works out to a full 8 whenever `column` is already a multiple of 8.

`\n` is simpler: it just starts a new line and resets the column count to 0.

**Your task:** using **one single `print()` statement** (one string, with `\t` and `\n` characters embedded in it — no other print calls, and no literal space characters anywhere — every bit of horizontal spacing must come from `\t`), display this hexagon outline:

```
                *
        *               *
*                               *
*                               *
        *               *
                *
```

Six rows. Every `*` sits on a multiple of 8 (columns 0, 8, 16, 24, and 32 are all in play), and the shape is symmetric top to bottom.

---

## Exercise 4 — Find the Bugs

The program below is supposed to compute a coffee order total after a percentage discount. It has exactly **three** mistakes — one of each of these types:
- a **syntax error** (Python won't even start running the file)
- a **runtime error** (Python starts running, then crashes partway through)
- a **logic error** (the program runs to completion and prints something, but the number is wrong)

```python
price_per_cup = float(input("Price per cup: "))
num_cups = int(input("How many cups: "))
discount_percent = int(input("Discount percent (0 if none): "))

subtotal = price_per_cup * num_cup
total = subtotal - discount_percent

print("Subtotal: $" + str(subtotal)
print("Total after discount: $" + str(total))
```

**Your task:** find all three mistakes. For each one, say which of the three categories it belongs to. Then fix all three so the program produces correct output; For a price of `4.50`, `3` cups, and a `10` percent discount, the corrected program should print:

```
Subtotal: $13.5
Total after discount: $12.15
```

---

## Exercise 5 — Discover: Compound Assignment

Three operators we haven't covered in class: `+=`, `-=`, `*=`. Figure out what they do before using them.

**Step 1 — experiment.** In the interpreter (or a scratch file), predict the output of each block *before* you run it, then check:

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

In one sentence each, say what `+=`, `-=`, and `*=` do — and what plain assignment statement each one is shorthand for (e.g., `x += 3` is shorthand for `x = ____`).

**Step 2 — apply it.** Now use what you just figured out to track a trivia team's score through three rounds — one compound assignment operator per round, no plain `score = score ...` allowed:

- Start `score` at `0`.
- Round 1: the team answers a bonus question worth 10 points.
- Round 2: an incorrect buzz-in costs them 4 points.
- Round 3: a wager round doubles whatever the score currently is.

Print the score after each round, clearly labeled.
