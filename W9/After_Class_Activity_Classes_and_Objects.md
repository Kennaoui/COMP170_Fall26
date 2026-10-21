# COMP 170 — After-Class Activity: Classes and Objects

## Exercise 1 — Model a class

Answer the question in **Activity 1, Part A** on [Slide 20 from today's lecture](https://sakai.luc.edu/access/content/group/COMP_170_002_1995_1266/resources/Classes_Objects_v5.pdf).

## Exercise 2 — LibraryBook

Write class **LibraryBook**. Its `__init__` takes `title: str` and `is_checked_out: bool = False`. Run the starter lines below and match the output.

```python
class LibraryBook:
    """A book in a library."""
    ...

book1 = LibraryBook("The Little Prince")
book2 = LibraryBook("The Hobbit", True)
print(book1.title, book1.is_checked_out)
print(book2.title, book2.is_checked_out)
```

**Expected output**

```text
The Little Prince False
The Hobbit True
```

## Exercise 3 — Find and fix the bugs

First, predict what happens when this program runs. Then find and fix the **two bugs** so that the program produces the expected output.

```python
class Student:
    """A student with a name and a GPA."""

    def __init__(name: str, gpa: float = 0.0) -> None:
        """Create a student."""
        self.name = name
        gpa = gpa

s = Student("Kim", 3.5)
print(s.gpa)
```

**Expected output after the fix**

```text
3.5
```
