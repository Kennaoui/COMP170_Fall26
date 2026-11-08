# Three List Problems

## Problem 1: Find the First Student Who Passed (Linear Search)

A teacher stores students' quiz scores in a list, in the order they submitted their quizzes.

Write `first_passing_score(scores: list[int]) -> int` that searches **from left to right** and returns the **index of the first score that is at least 7**. If no student passed, return `-1`.

```python
first_passing_score([3, 5, 8, 6, 9])  # 2
first_passing_score([7, 4, 9])        # 0
first_passing_score([2, 5, 4])        # -1
first_passing_score([])               # -1
```

**Constraints:** Use a loop and indexes; do not use `index()`, `count()`, `in`, or built-in search helpers. Try both a `for` loop and a `while` loop. Do not use `break` or multiple `return` statements.

### Before coding

- What should the function return if the first score qualifies? What if none qualify?
- How can we remember the **first** matching index without overwriting it later?
- A **`for`** or **`while`** loop? what is the difference in this case?

**Linear search:** Examine elements one at a time until a match is found or the list is exhausted. In the worst case, it examines all `n` elements. A `while` loop is useful here when we want to stop as soon as a match is found.

## Problem 2: Reverse a List in Place

Write `reverse(items: list[int]) -> None` to **reverse the original list**.

```python
numbers = [10, 20, 30, 40, 50]
reverse_in_place(numbers)
print(numbers)  # [50, 40, 30, 20, 10]
```

**Constraints:** Do not use `reverse()`, `reversed()`, or slicing (`[::-1]`).



## Problem 3: Remove Failing Scores While Traversing

Write `remove_failing_scores(scores: list[int]) -> None` to remove **every score below 7**, modifying the original list.

```python
scores = [4, 3, 8, 5, 9, 2]
remove_failing_scores(scores)
print(scores)  # [8, 9]
```

**Constraints:** Do not use `filter()` or create a replacement list.

### Before coding

- What happens to the positions of later elements after `pop(i)`?
- Should we increment `i` after removing an element? Why or why not?
- What happens when **two failing scores appear consecutively**?
- What loop condition prevents an out-of-range access as the list gets shorter?

