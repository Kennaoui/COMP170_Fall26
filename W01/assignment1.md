# Week 1 Assignment — First Python Programs

## General Instructions

For each exercise:

1. Use the terminal to create or open the required file in Vim.
2. Write and save your program.
3. Run the program from the terminal.
4. Read the output or error message.
5. Return to Vim when corrections are needed.
6. Repeat this cycle until the final program works as expected.

Place your name at the beginning of every Python file:

```python
# Name: Your Name
```

Your terminal screenshots must be readable and must show:

- The command you entered
- The resulting output or error message
- Enough of the terminal window to show that you ran the appropriate file


Note: In a Python file, any line that begins with # is a comment: Python does not execute it as code, so it can be used to add notes or explanations for the reader.

---

## Exercise 1 — A Short Introduction

Write a program that stores and displays information about you.

### Instructions

Create a file named `introduction.py`.

Declare variables that store:

- Your name
- Your major or intended major
- Your favorite food
- A place you would like to visit

Then use `print()` to display the information in a short, readable introduction.

Your program must include:

- At least four appropriately named variables
- Both single and double quotation marks as string delimiters
- At least one string containing a quotation mark
- At least one newline escape sequence, `\n`
- At least one tab escape sequence, `\t`
- At least one `print()` statement that receives multiple values separated by commas
- One triple-quoted string extending over more than one line

Your output does not need to match a specific example, but it should be organized and easy to read.

### Written Questions

Answer these questions under **Exercise 1** in your PDF:

1. List the names of the four main variables in your program.
2. Explain why each name is a valid Python identifier. (1 to 2 lines)
3. What is the difference between writing `\n` and `\t` inside a string? (1 to 2 lines)
4. Describe one change you made during the write–run–edit cycle. (2 to 3 lines)

### What to turn in

Submit:

- `introduction.py`
- In `week01_report.pdf`:
  - Your answer to written questions 1 to 4
  - A screenshot showing the command used to run the program
  - The complete output produced by the final program 

---

## Exercise 2 — Finding and Correcting Errors

Reading and correcting errors is an essential part of programming. In this exercise, you will begin with a program that contains several errors and repair it gradually.

### Instructions

Create a file named `errors.py` and copy the following code into it exactly as written:

```python
print(welcome_message)

welcome-message = "Welcome to COMP 170!"
2nd_message = 'We are learning Python.'

print(welcome-message)
print("The student said, "Python is fun!"")
```

Do not correct the code before running it for the first time.

Follow this process:

1. Run the program.
2. Read the error message.
3. Take a screenshot of the terminal showing the command and the error.
4. Correct one problem.
5. Run the program again.
6. Continue until the program runs successfully.

Your final program must:

- Preserve the two original messages
- Display both messages
- Display the sentence containing `"Python is fun!"`
- Use valid variable names
- Declare every variable before using it
- Run without errors

### Written Question

Answer this question under **Exercise 2** in your PDF:

For each error, briefly describe the problem, include the relevant error message when available, and explain the correction you made. (1-2 lines per error)

### What to Turn In

Submit:

- The corrected `errors.py`
- In `week01_report.pdf`:
  - Your answer to the Written Question
  - At least one screenshot showing the command and an error message
  - A screenshot showing the final command and the successful output

---

## Exercise 3 — Values, Types, and Operations

Python does not require us to write a variable’s type when declaring the variable. However, every value still has a type, and that type determines which operations Python can perform.

### Instructions

Create a file named `types.py` and begin with the following variables:

```python
first_number = 5
second_number = 3
first_word = "COMP"
second_word = "170"
```

Before running the program, predict the type of each variable and record your predictions in the PDF.

Next, complete the program so that it:

step 1. Uses `type()` to display the type of each variable.
step 2. Adds `first_number` and `second_number` and displays the result.
step 3. Adds `first_word` and `second_word` and displays the result.
step 4. Displays a label before each result so the output is easy to understand.
step 5. After completing those steps, add and run this statement:

```python
print(first_number + first_word)
```

Take a screenshot of the execution result. Read it carefully and try to determine what it means.

step 6. Finally, turn the statement from question 5 into a comment. Run the program again and confirm that the submitted version works successfully.

### Written Questions

Answer these questions under **Exercise 3** in your PDF:

1. Complete the following table:

| Variable       | Predicted type | Type reported by Python |
|  ---------     |  ---------     |        ---------        |
| `first_number` |                |                         |
| `second_number`|                |                         |
| `first_word`   |                |                         |
| `second_word`  |                |                         |

2. What result did Python produce for `first_number + second_number`? 
3. What result did Python produce for `first_word + second_word`?
4. The same `+` operator was used in both cases. Why did it produce different kinds of results? (1 to 2 lines)
5. What message appeared when you tried to evaluate `first_number + first_word`? 
6. Identify the types of the two values involved in that unsuccessful operation. 
7. Explain in your own words why Python does not permit that operation. (2 to 3 lines)

### What to Turn In

Submit:

- `types.py`, with the statement from step 5 turned into a comment
- In `week01_report.pdf`:
  - Your completed type table
  - Your answers to Questions 1–7
  - A screenshot showing the results produced by `type()`
  - A screenshot showing the mixed-type error
  - A screenshot showing the final successful execution

---

## Files to Submit

Submit the following four files on Sakai:

1. `introduction.py`
2. `errors.py`
3. `types.py`
4. `week01_report.pdf`

The three `.py` files contain your Python programs. The PDF contains:

- Screenshots of the terminal showing the requested commands and results
- Error messages, when requested
- Your answers to the written questions

Do not copy all your Python code into the PDF. Your code will be submitted separately in the `.py` files.

---

## PDF Organization

Organize `week01_report.pdf` using these headings:

```text
Exercise 1
Exercise 2
Exercise 3
```

Place each screenshot near the question or explanation to which it relates. Screenshots should be large enough to read without excessive zooming.
