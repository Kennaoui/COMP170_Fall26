# COMP 170 — Week 1 Recap

During our first week, we became familiar with the basic tools and ideas we will use throughout the course.

## Terminal and Vim

We practiced using the **terminal** to navigate the computer, create and open files, and run Python programs. We also used **Vim** to write and edit code.

Remember the basic **write–run–edit cycle**:

1. Write or edit your program in Vim.
2. Save the file.
3. Run the program from the terminal.
4. Read the result or error message.
5. Return to Vim and make the necessary changes.

You will repeat this cycle constantly while programming.

## The `print()` Function

We used `print()` to display information on the screen. A string can be written using either single or double quotation marks:

```python
print("Hello!")
print('Welcome to COMP 170!')
```

Triple quotation marks can delimit strings that extend over multiple lines:

```python
message = """Welcome to COMP 170.
We are learning Python!"""
print(message)
```
The opening and closing delimiters must match.

We can also print several strings or values at once by separating them with commas:

```python
course = "COMP 170"
print("Welcome to", course)
```

### Special Characters in Strings

A backslash introduces an **escape sequence**. The backslash itself and the quotation mark used to delimit the string must be escaped when they appear inside that string.

| Escape | What it means |
| --- | --- |
| `\\` | backslash `\` |
| `\"` | double quote `"` |
| `\'` | single quote `'` |
| `\n` | newline |
| `\t` | tab |

Example:

```python
print("She said, \"Hello!\"")
print("First line\nSecond line")
```

## Variables

A **variable** is a name that refers to a value. We create a variable by assigning a value to it:

```python
student_name = "Maya"
credits = 3
```

After a variable has been created, we can use its name to access its value:

```python
print(student_name)
```

Remember: **declare first, then use**. Python must encounter the assignment before it can use the variable. Otherwise, the program produces an error.

## Identifiers

An **identifier** is a name used for a variable, function, or another element of a program. In Python, an identifier must:

- Start with a **letter** (`a–z` or `A–Z`) or an **underscore** (`_`).
- Contain only **letters, digits, or underscores**.
- **Not start with a digit**.
- **Not contain special characters** such as `-`, `>`, or quotation marks.
- **Not be a reserved Python keyword**.

Examples:

```python
course_name = "COMP 170"  # Valid
week1 = "Introduction"    # Valid
# 1week = "Introduction"  # Invalid: starts with a digit
# course-name = "COMP 170" # Invalid: contains a hyphen
```

## Errors

We encountered our first programming error. Errors are a normal part of programming. When one occurs, carefully read the message, identify where the problem happened, and return to the **write–run–edit cycle**.

## Types

Every value in Python has a **type**, such as a string, integer, or decimal number. Python usually **infers** the type from the assigned value, so we do not explicitly write the variable's type when declaring it:

```python
message = "Hello"  # string
number = 5          # integer
price = 4.99        # floating-point number
```

Types are still important. Python uses them to determine which operations are legal and what an operation means. Sometimes the same operator behaves differently depending on the types involved:

```python
print(2 + 3)           # 5: addition of integers
print("Hello" + "!") # Hello!: concatenation of strings
```

## The `type()` Function

We did not get a chance to explore `type()` in class. This function allows us to see the type of the value or variable given as input:

```python
course = "COMP 170"
credits = 3

print(type(course))   # <class 'str'>
print(type(credits))  # <class 'int'>
```

Use `type()` when you want to check what kind of value Python has inferred.

## Quick Reference Card

### Bash

```text
pwd              Where am I?
ls               What is here?
ls -l            What is here, with details?
mkdir name       Create a directory
cd name          Enter a directory
cd ..            Go up one directory level
cd ~             Go to your home directory
python3 file.py  Run a Python program
vim file.py      Open a file in Vim
```

### Vim

```text
i       Enter Insert mode and start typing
Esc     Return to Normal mode
:w      Save the file
:q      Quit Vim
:wq     Save and quit
:q!     Quit without saving
```
