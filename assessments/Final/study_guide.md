# COMP 170-002 Final Exam Study Guide

**Format: a one-hour exam with multiple-choice and short-answer questions. It is cumulative and covers the whole semester. You may bring one letter-size sheet of handwritten notes.**

The final pulls together what you practiced in the three quizzes and the ten assignments. It focuses on the ideas that came back all semester: functions, decisions, loops, lists and strings, classes and objects, and the Week 11–13 data tools (tuples and dictionaries).

## How to prepare

1. **Revise the three quizzes.** Redo each question without looking at your answers, then compare. Pay most attention to the questions you missed.
   - Quiz 1 (Weeks 1–6): [practice questions](https://github.com/Kennaoui/COMP170_Fall26/blob/main/assessments/Quiz1/practiceQuestions_weeks_1_to_6.pdf) and [solutions](https://github.com/Kennaoui/COMP170_Fall26/blob/main/assessments/Quiz1/practiceQuestions_weeks_1_to_6_solution.pdf)
   - Quiz 2: [Quiz 2 debrief](https://sakai.luc.edu/access/content/group/COMP_170_002_1995_1266/resources/Quiz2/Quiz2_Debrief.pdf)
   - Quiz 3 (Weeks 10–12): [Quiz 3 study guide](https://github.com/Kennaoui/COMP170_Fall26/blob/main/assessments/Quiz3/Study_Guide.md)
2. **Go through all ten assignments.** Reread each assignment, then your own submission and the feedback you got. Ask yourself whether you could rewrite each function on paper, without running it. All assignments are on [Sakai Assignments](https://sakai.luc.edu/portal/site/COMP_170_002_1995_1266/tool/67a204d4-5394-4bcd-9700-e36298324595); the instructions are in the [course GitHub repository](https://github.com/Kennaoui/COMP170_Fall26).
3. **Work through the topic sections below.** Each one links its slides or notebook. Make sure you can answer every question listed under it.
4. **Practice by hand.** On the exam you trace code, predict output, spot bugs and write short functions on paper, with no computer.

## Assignments to review

Go through all ten assignments, but focus on these four.

| Assignment | Why focus on it |
| --- | --- |
| [Assignment 10](https://github.com/Kennaoui/COMP170_Fall26/blob/main/W_13/assignment10.md): Playlist Manager | It is your only practice on tuples and dictionaries, and it also covers search, deleting while traversing and aliasing. |
| [Assignment 9](https://github.com/Kennaoui/COMP170_Fall26/blob/main/W_10/while_loop_assignment.md): While loops | It covers tracing while loops, sentinels, retry loops and fenceposts, which are common in trace and find-the-bug questions. |
| [Assignment 8](https://github.com/Kennaoui/COMP170_Fall26/blob/main/W9/classes_and_objects_assignment.md): Points and Houses | It covers writing and using a class: `__init__`, `self`, and methods that read or change an object. |
| [Assignment 7](https://github.com/Kennaoui/COMP170_Fall26/blob/main/W8/Lists_Strings_Assignment.md): Lists and strings | It covers loops over lists and strings with indexing and accumulators, which most short answers build on. |

## On the final

### 1. Running Python; values, types and expressions (Weeks 1–2)

Sources: [Week 1 notebook](https://github.com/Kennaoui/COMP170_Fall26/blob/main/W01/notebook.ipynb), [Week 2 notebook](https://github.com/Kennaoui/COMP170_Fall26/blob/main/W02/notebook.ipynb), Assignments 1–2.

- Two ways to run Python code: write a `.py` file and run it from the shell with `python3 file.py` (or `python file.py`), or type `python3` alone to open interactive mode (the `>>>` prompt), where each line runs as soon as you press Enter. Type `exit()` to leave interactive mode.
- `str`, `int`, `float`, `bool`; `type()`; converting with `int()`, `float()`, `str()`.
- Operator precedence; `/` vs `//`; `%` for remainders.
- Syntax errors vs runtime errors vs wrong results.

Questions you should be able to answer:

- What is the difference between running a `.py` file with `python3` and typing code in interactive mode? Why does a bare expression such as `2 + 3` show its value at `>>>` but print nothing in a `.py` file? Which shell command executes a .py file (for example, python3 hello.py), and how do you start interactive mode and leave it with exit()?
- What does an expression evaluate to, and what is its type?
- Why does `"5" + 3` fail, and how do you fix it?
- What do `17 // 5` and `17 % 5` give, and when do you use each?

### 2. Functions (Weeks 3 and 8)

Sources: [Week 3 notebook](https://github.com/Kennaoui/COMP170_Fall26/blob/main/W03/notebook.ipynb), [Stronger Functions slides](https://sakai.luc.edu/access/content/group/COMP_170_002_1995_1266/resources/COMP170_Stronger_Functions.pdf), Assignment 3.

- Defining and calling functions; parameters vs arguments; local variables.
- `return` vs `print()`: a function that prints gives back `None`.
- Contracts: docstring, type annotations, preconditions, input validation.
- One focused job per function; `main()` coordinates the program.

Questions you should be able to answer:

- What does a call evaluate to when the function has no `return`?
- Given a function and a call, what is printed and what is returned?
- What precondition does a function need, and what happens if the caller breaks it?
- How would you split a long program into small functions plus `main()`?

### 3. Decisions (Week 5)

Sources: [Relational expressions, Boolean logic, conditionals slides](https://sakai.luc.edu/access/content/group/COMP_170_002_1995_1266/resources/slides.pdf), Assignment 5.

- Relational operators; `=` vs `==`; `and`, `or`, `not`.
- `if` / `elif` / `else`: only the first true branch runs.
- Testing boundary values.

Questions you should be able to answer:

- Which branch runs for a given input?
- Why do separate `if`s and an `if/elif` chain give different results?
- Which inputs would you test to check every boundary of a condition?

### 4. For loops and accumulators (Week 4)

Sources: [For loops slides](https://sakai.luc.edu/access/content/group/COMP_170_002_1995_1266/resources/for_loops.pdf), [Week 4 code](https://github.com/Kennaoui/COMP170_Fall26/tree/main/W04), Assignment 4.

- `for` with `range(start, stop, step)`; off-by-one errors.
- Accumulators: start, update, finish (sum, count, product).

Questions you should be able to answer:

- Which values does `range(3, 20, 4)` produce?
- What does a short loop print, step by step?
- Where must an accumulator be set to its starting value, and why?

### 5. Lists (Weeks 6–7 and 11)

Sources: [Lists slides](https://sakai.luc.edu/access/content/group/COMP_170_002_1995_1266/resources/Lists_v2.pdf), [Week 6 code](https://github.com/Kennaoui/COMP170_Fall26/tree/main/W06), [Week 11 materials](https://github.com/Kennaoui/COMP170_Fall26/tree/main/W_11) (notebook and `list_problems.md`), Assignments 6, 7 and 10 (Parts 1, 2 and 6).

- 0-based indexing, negative indexes, slicing, `len()`.
- Looping over elements vs over indexes.
- `append`, `insert`, `pop`, `remove`, `index`, `in`.
- Writing your own average, maximum and count, without built-ins; the empty-list case.
- Linear search that returns the first index, or -1 if not found.
- Removing items while traversing: why a `for` loop skips elements, and the while-loop fix.
- Swapping two elements; reversing a list in place.
- Lists are mutable; two names can refer to the same list (aliasing).

Questions you should be able to answer:

- What is the list after a sequence of method calls?
- When do you need to loop over indexes instead of elements?
- What should a function return for an empty list?
- What does a search function return when the item is missing, and why -1?
- Which element gets skipped when you remove during a `for` loop?
- After `b = a` and a change through `a`, what does `b` show?

### 6. Strings (Weeks 6–8)

Sources: [Strings slides](https://sakai.luc.edu/access/content/group/COMP_170_002_1995_1266/resources/Strings_Slides.pdf), [Lists and Strings practice](https://github.com/Kennaoui/COMP170_Fall26/blob/main/W8/Lists_Strings_Practice.pdf), Assignment 7.

- Strings are immutable sequences: indexing, slicing, looping over characters.
- Methods: `upper`, `lower`, `strip`, `split`, `find`; function vs method (`len(s)` vs `s.upper()`).
- Building a new string with an accumulator.

Questions you should be able to answer:

- What does a slice such as `s[1:4]` or `s[::-1]` return?
- Why does `s[0] = "A"` fail?
- What does `"a,b,,c".split(",")` return?

### 7. Classes and objects (Week 9)

Sources: [Classes and Objects slides](https://sakai.luc.edu/access/content/group/COMP_170_002_1995_1266/resources/Classes_Objects_v6.pdf), [Week 9 code (BankAccount)](https://github.com/Kennaoui/COMP170_Fall26/tree/main/W9), Assignments 8–9.

- A class is the blueprint; each object has its own state.
- `__init__`, `self`, instance attributes, methods, `__str__`.
- Methods that only read state vs methods that change it.
- Several objects of the same class; one method that takes another object (`p.distance(q)`).

Questions you should be able to answer:

- What does a short program that creates and changes two objects print?
- Why does every method have `self` as its first parameter?
- Which methods change the object, and which only return information?
- What should a method do when asked for an invalid change, such as withdrawing more than the balance?

### 8. While loops, sentinels and retry loops (Week 10)

Sources: [While Loops and Sentinels slides](https://sakai.luc.edu/access/content/group/COMP_170_002_1995_1266/resources/10_While_Loops_Sentinels.pdf), [Week 10 code](https://github.com/Kennaoui/COMP170_Fall26/tree/main/W_10), Assignment 9.

- The three parts of a while loop: set up, test, update. A missing update gives an infinite loop.
- Sentinel loops and the priming read.
- Fencepost problems ("1, 2, 3" without a trailing comma).
- Retry loops that repeat until the input is valid.
- For vs while: a known count vs an unknown count.

Questions you should be able to answer:

- How many times does a given while loop run, and what does it print?
- Why must the read happen before the loop and again at the end of the body?
- What is wrong with a loop that counts the sentinel as data?
- How would you rewrite a `for` loop over `range()` as a while loop?

### 9. Tuples (Week 12)

Sources: [Tuples slides](https://github.com/Kennaoui/COMP170_Fall26/blob/main/W_12/tuples_slides.pdf), [Tuples handout](https://github.com/Kennaoui/COMP170_Fall26/blob/main/W_12/tuples_handout.pdf), Assignment 10 Part 3.

- Creating tuples, including the one-element trap `(5,)`.
- Indexing, slicing and unpacking; a function that returns several values as a tuple.
- Tuples are immutable: when to choose a tuple over a list.

Questions you should be able to answer:

- What is the type of `(5)` and of `(5,)`?
- What happens when you try to change an item of a tuple?
- How do you unpack a returned tuple into three variables?

### 10. Dictionaries (Week 13)

Sources: [Dictionaries slides](https://github.com/Kennaoui/COMP170_Fall26/blob/main/W_13/dictionaries_slides.pdf), [Dictionaries handout](https://github.com/Kennaoui/COMP170_Fall26/blob/main/W_13/dictionnaries_handout.pdf), Assignment 10 Part 4.

- Key–value pairs; keys are unique and immutable.
- `d[key]` vs `d.get(key)`; adding, updating and deleting entries; `in`, `keys()`, `values()`, `items()`.
- The counting pattern: add a new key with 1, or add 1 to an existing key.

Questions you should be able to answer:

- What does `d["x"]` do when `"x"` is missing, and what does `d.get("x")` do?
- What dictionary does a counting loop build from a short list?
- Why can a tuple be a key but a list cannot?

## Be able to tell apart

- `return` vs `print()`
- `=` vs `==`
- `/` vs `//` vs `%`
- separate `if`s vs an `if/elif/else` chain
- `for` (known number of repetitions) vs `while` (repeat until a condition changes)
- a sentinel loop vs a retry loop
- a function vs a method (`len(s)` vs `s.upper()`)
- a class vs an object
- a method that reads state vs a method that changes it
- modifying a list in place vs building a new list
- two names for one list (aliasing) vs a copy
- list (mutable) vs tuple (immutable) vs dictionary (key–value pairs)
- `d[key]` vs `d.get(key)`

## Not on the final

These topics are not on the final:

- Shell commands other than running Python, Vim and Git.
- Number systems (binary, hex, base conversion by hand) and memorizing ASCII codes.
- The `math` module's functions.
- Drawing shapes with nested loops (staircases, triangles, diamonds).
- Encapsulation beyond the basics (private attributes and their rules).
- Assertions.
- `try/except` and exceptions.
- Designing a whole program or writing full pseudocode.
- Files: writing and reading files with `open()` (Assignment 10, Part 5).
- The final project.

**Forbidden in your code answers:** `break`, `continue` and `while True`, or any advanced tool or concept not covered in class. Do not use them in any code you write on the exam. Control every loop with its condition.
