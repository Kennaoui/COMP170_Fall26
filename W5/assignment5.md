# COMP 170 — Assignment: Conditions, Modules, and Lists

Create one Python file for each exercise. Place pseudocode in comments at the top of each file. Every function must have type annotations, a docstring, and one focused job. Use a `main()` function to coordinate each program and call it at the end of the file. Follow the Programmer's Pact.

## Exercise 1 — Museum admission

Create `museum_admission.py`. Regular admission costs $18. Admission is free for visitors younger than 12 or at least 65. Visitors aged 12 through 64 with a student ID pay $12.

Write `admission_price(age: int, has_student_id: bool) -> int` to return the correct price. Use conditional execution and at least one compound Boolean expression with `and` or `or`.

In `main()`, ask for the visitor's age and whether they have a student ID, then print the admission price. You may assume the age is nonnegative and that the student-ID answer is `yes` or `no`. Check your program with ages 11, 12, 64, and 65, including both a student and a nonstudent between 12 and 64.

## Exercise 2 — Distance to a destination

Create `trip_distance.py`. Import the `math` module and use functions from it to calculate the straight-line distance between two points (x1, y1) and (x2, y2):

distance = square root of ((x2 - x1)² + (y2 - y1)²)

Write `distance(x1: float, y1: float, x2: float, y2: float) -> float` to return the distance. In `main()`, ask for the coordinates of both points, print the distance rounded to two decimal places, and report whether the destination is **nearby** (distance at most 5) or **farther away** (distance greater than 5). Test a distance below 5, exactly 5, and above 5.

## Exercise 3 — Update a reading list

Create `reading_list.py`. Begin with this list:

```python
books = ["Python Basics", "Algorithms", "Web Design"]
```

In `main()`, perform these operations in order. Print the entire list after each of the first three changes:

1. Ask the user for a book title and add it to the end of the list.
2. Replace `"Web Design"` with `"Data Structures"`.
3. Remove `"Python Basics"`.
4. Print the number of books and the title of the first book.

Use list operations to change the list. You may assume the starting list has the contents shown above.

## Submission

Submit all three Python files: `museum_admission.py`, `trip_distance.py`, and `reading_list.py`.
