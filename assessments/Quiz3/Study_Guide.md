# COMP 170-002 Quiz 3 Study Guide

**Monday 11/23, 12 questions in 50 minutes on Sakai: multiple choice and short answer.**

## On the quiz

- Short answers ask you to **read** code (trace what it does or prints), **explain** it, **correct** it (find and fix the bug), or **modify** it.
- Main focus of the quiz: **while loops** and the **list algorithms** built with them (search, delete, swap, reverse). Expect to trace loops step by step and count how many times things happen.
- Course rules apply on every answer: no `break`, `continue`, or `while True:`. The stopping rule goes in the `while` condition.
- Each chapter below ends with **questions you should be able to answer**. They tell you what to look for and revise; they are not the quiz questions themselves.

## While loops ([While loops slides](https://sakai.luc.edu/access/content/group/COMP_170_002_1995_1266/resources/10_While_Loops_Sentinels.pdf))

- **Definition.** A `while` loop repeats its body as long as its condition is True. The condition is checked before every repetition, so the body can run zero times (slides pp. 12–15).
- **Three questions for every while loop.** Initialize (what is set before the loop), condition (what means "keep going"), update (what changes so the loop can stop). No initialization gives an error at the first check; no update gives an infinite loop (pp. 16–20, 25–26).
- **Tracing.** Use a table with one row per condition check: the variables, whether the condition is True, and what is printed. The condition is checked one more time than the body runs; the last check is the False one that ends the loop. Know the value of the loop variable after the loop (pp. 21–24).
- **Order inside the body matters.** Moving the update or the input line changes the result: an error, a wrong total, or an infinite loop (pp. 45–47).
- **for vs while.** Use `for` to visit every item of a string or list or to repeat a known number of times. Use `while` to visit every item of a string (handle index update manually) or list or when the number of repetitions is not known in advance (until the user types "quit", until a value reaches a threshold or until a value is found). Any `range` loop can be rewritten as a while loop (pp. 27–36).
- **Threshold loops.** Repeat until a value reaches a limit, counting the steps: years until a balance reaches a goal (pp. 30–31, `years_to_reach` in `W_10/while_examples.py`); minutes to charge a battery ([assignment](https://github.com/Kennaoui/COMP170_Fall26/blob/main/W_10/while_loop_assignment.md) Exercise 1a); steps until n reaches 1 (Exercise 2).

**Questions you should be able to answer**

1. What does a while loop do, and when is its condition checked?
2. What are the three parts every while loop needs, and what goes wrong if each one is missing?
3. What causes an infinite loop, and how do you fix one?
4. Can a while loop run zero times? When?
5. Why is the condition checked one more time than the body runs?
6. What is the value of the loop variable after the loop ends?
7. How do you trace a while loop in a table, and what do you write in each row?
8. How do you choose a condition that makes a loop stop at the right value (`<` vs `<=`, `>` vs `>=`)?
9. How can moving one line inside the body change the output?
10. When is a `for` loop the better choice, and when is a `while` loop better?
11. How do you rewrite a `for i in range(...)` loop as a while loop?
12. Why would you simulate a process step by step with a while loop instead of using one calculation?
13. What does a counter variable inside a loop tell you at the end?

## Sentinels and the fencepost pattern ([While loops slides](https://sakai.luc.edu/access/content/group/COMP_170_002_1995_1266/resources/10_While_Loops_Sentinels.pdf))

- **Sentinel.** A special value that signals the end of input. It is never processed as data. Pick a value that can never be valid data: -1 for prices or scores (not 0, which is a real score), an empty line for names, "quit" for text (slides pp. 48–53).
- **Fencepost idea.** A fence with n sections needs n + 1 posts. A sentinel loop processing n values makes n + 1 reads: the n values, then the sentinel (pp. 55–58).
- **The pattern: read, check, process, read again.** A priming read before the loop, the check in the `while` condition, process the value, and read the next value as the last line of the body (p. 59).
- **The classic bug: reading at the top of the body.** The sentinel is processed before the check sees it, so it is added to the total (12.50, 8.00, -1 gives 19.5 instead of 20.5) (pp. 60–62).
- **Fencepost in output.** To print items with a separator between them and none at the end (`1, 2, 3` or arrows), print the first item before the loop, then "separator + item" inside it (`draw_fence` in `W_10/while_examples.py`).
- **In the [assignment](https://github.com/Kennaoui/COMP170_Fall26/blob/main/W_10/while_loop_assignment.md).** Exercise 1b: the driving loop ends when the user enters the sentinel 0. Exercise 2, step 2: print the 3n+1 sequence with arrows and no arrow at the end.

**Questions you should be able to answer**

1. What is a sentinel value, and why is it never processed as data?
2. How do you choose a good sentinel for a given kind of input (ages, scores, names, text)?
3. Why can 0 be a bad sentinel for scores, and why can an empty string be a bad sentinel for text?
4. What is a priming read, and why is it needed?
5. Where must the next read go inside the loop body, and why?
6. What goes wrong when the input is read at the top of the loop body?
7. What does a sentinel loop return if the user enters the sentinel first?
8. To process n values, how many times does a sentinel loop read input?
9. What is the fencepost idea (n sections, n + 1 posts), and how does it connect to sentinel loops?
10. How do you print a list of items with separators between them but not at the end?
11. What is an off-by-one error, and how does the fencepost pattern avoid it?
12. In a sentinel loop, which variables need a starting value before the loop?

## Retry loops ([While loops slides](https://sakai.luc.edu/access/content/group/COMP_170_002_1995_1266/resources/10_While_Loops_Sentinels.pdf))

- **Retry loop.** Repeat an attempt until it succeeds. For input validation: ask for a value, check it, and ask again while it is invalid. Same shape as a sentinel loop, but the condition means "still invalid" (slides pp. 63–65).
- **Writing the condition.** The loop keeps going while the input is invalid: a valid age from 1 to 120 gives `while age < 1 or age > 120:`; a y/n answer gives `while answer != "y" and answer != "n":`. With `or` in the y/n check, the condition is always True, so the loop never ends.
- **`if` is not a retry.** An `if` checks only once, so a second invalid entry is accepted.
- **Re-read inside the loop.** A loop that prints an error but never asks again is infinite.
- **Checking text before converting it.** `score.isdigit() and 0 <= int(score) <= 10`: `and` is evaluated left to right and stops at the first False, so `int()` is never called on text like "abc" (`get_quiz_score_v2` in `W_10/in_class_activity.py`).
- **Examples in the [assignment](https://github.com/Kennaoui/COMP170_Fall26/blob/main/W_10/while_loop_assignment.md).** Exercise 1b: retry on the car choice, on a distance greater than 0, and on a charging target with 0 < target ≤ capacity; write the retry once and reuse it. Exercise 2: re-ask until the starting number is at least 1, and until the answer is y or n.

**Questions you should be able to answer**

1. What is a retry loop, and when do you need one?
2. How is a retry loop like a sentinel loop, and how is it different?
3. Why does an `if` statement not work for validating input more than once?
4. How do you write a condition that is True while the input is invalid?
5. When should the condition use `and`, and when `or`? (Ranges like 1 to 120, choices like y or n.)
6. Why does `answer != "y" or answer != "n"` never become False?
7. What happens if the loop body prints an error but never asks again?
8. In what order are the parts of an `and` condition checked, and why does that order matter?
9. Why check `isdigit()` before calling `int()`?
10. How many times is the error message printed for a given list of inputs?
11. Why put the retry logic in one function instead of copying the loop for every prompt?
12. What value does a retry function return, and when?

## Linear search ([Weekly materials](https://github.com/Kennaoui/COMP170_Fall26/tree/main/W_11))

- **Linear search.** Check the items one at a time, left to right, until a match is found or the list ends. It works on unsorted lists. In the worst case (no match, or the match is last) it checks all n items (`notebook.ipynb` Section 1).
- **What it returns.** The index of the first match, not the value at that index; -1 when there is no match. -1 is never a valid position for "found", but `items[-1]` is legal Python (the last item), so check the result before using it as an index.
- **while version.** The condition combines "still in bounds" and "not found yet": `while i < len(items) and result == -1:`. The loop stops at the first match (`linear_search_problem.py`).
- **for version.** `for i in range(len(items))` visits every index. Without a guard such as `and result == -1`, each new match overwrites the last one, so it returns the last match instead of the first.
- **Bounds check first.** In `i < len(items) and ...`, the bounds test comes first; `and` stops at the first False, so `items[i]` is never read past the end.
- **Edge cases.** Empty list, match at index 0, match at the last index, no match, duplicates.
- **In the [list problems](https://github.com/Kennaoui/COMP170_Fall26/blob/main/W_11/list_problems.md).** Problem 1: index of the first score that is at least 7, or -1; write it with a `for` loop and a `while` loop, without `index()`, `in`, or `break`.

**Questions you should be able to answer**

1. What is linear search, and how does it move through a list?
2. What does linear search return when it finds a match? When it does not?
3. What is the difference between returning an index and returning a value?
4. Why is -1 used for "not found"? Why is it still risky to use the result as an index without checking it?
5. What does linear search return for an empty list?
6. What two things does the while condition check, and why are both needed?
7. Why must the bounds check come before reading `items[i]`?
8. How do you make sure the search returns the first match, not the last?
9. Why does a `for` loop over every index find the last match unless you add a guard?
10. How does a while loop let the search stop as soon as it finds a match?
11. In the worst case, how many items does linear search check? When does that happen?
12. In the best case, how many items does it check?
13. Does linear search need the list to be sorted?
14. Does linear search change the list?

## Deleting while traversing ([Weekly materials](https://github.com/Kennaoui/COMP170_Fall26/tree/main/W_11))

- **`pop(i)`.** Removes the item at index i; every later item shifts one position left and the list gets shorter.
- **Why the `for` version fails.** `range(len(items))` is fixed before the loop starts, but each `pop(i)` shortens the list. The item that slides into position i is skipped, and the loop later reaches an index that no longer exists (`IndexError`). Two items to remove in a row show the skip (`notebook.ipynb` Section 3).
- **The while fix.** Keep your own index: if the item must go, `pop(i)` and do not increase i (a new item is now at position i, not yet checked); otherwise increase i. The condition `i < len(items)` is checked again each time, so it stays correct as the list shrinks.
- **Common bug.** Increasing i after every step, even after a removal, skips the next item.
- **Effect.** The function changes the original list and returns `None`.
- **Edge cases.** Nothing to remove (list unchanged), everything to remove (empty list), an empty list (body never runs).
- **In the [list problems](https://github.com/Kennaoui/COMP170_Fall26/blob/main/W_11/list_problems.md).** Problem 3: remove every score below 7 from the original list, without `filter()` or a new list, and its "Before coding" questions.

**Questions you should be able to answer**

1. What does `pop(i)` do to the list, and what happens to the items after index i?
2. Why does removing items inside `for i in range(len(items))` skip items?
3. Why can that `for` loop raise an `IndexError`?
4. Why does the case of two items to remove in a row show the bug?
5. After `pop(i)`, which item is now at position i? Has it been checked yet?
6. When should i increase, and when should it stay the same?
7. What goes wrong if i increases after every step, even after a removal?
8. Why does the condition `i < len(items)` stay correct while the list gets shorter?
9. Does the function change the original list or make a new one? What does it return?
10. How do you trace the list and the value of i step by step?
11. What happens when nothing needs to be removed? When everything does? When the list is empty?
12. How would you change the condition to remove a different kind of item (negatives, a given value)?

## Swapping and reversing a list ([Weekly materials](https://github.com/Kennaoui/COMP170_Fall26/tree/main/W_11))

- **Swapping two positions.** Save one value in a temporary variable first: `temp = items[i]`, `items[i] = items[j]`, `items[j] = temp`. Without `temp`, the first assignment overwrites a value before it is saved, so both positions end up equal (`swap` in `resversed_list.py`).
- **Out of place.** Build a new list: traverse the original from right to left and `append` each item. The original list does not change; the function returns the new list. Go backward with `range(len(items) - 1, -1, -1)` or with negative indexes -1 to -len(items) (`notebook.ipynb` Section 2, Approach A).
- **In place.** Swap the first and last items, then the second and second-to-last, and so on. Position i pairs with `len(items) - 1 - i`. The original list changes; the function returns `None` (Approach B).
- **Stop at the middle.** `len(items) // 2` swaps: 2 swaps for 4 or 5 items; the middle item of an odd-length list stays put. Swapping across the whole list swaps every pair back, so the list ends unchanged.
- **Edge cases.** An empty list or a one-item list needs 0 swaps.
- **Not allowed in these exercises:** `reverse()`, `reversed()`, and slicing `[::-1]`.
- **In the [list problems](https://github.com/Kennaoui/COMP170_Fall26/blob/main/W_11/list_problems.md).** Problem 2: reverse the original list in place.

**Questions you should be able to answer**

1. Why do you need a temporary variable to swap two items?
2. What happens to the list if you swap without one?
3. What is the difference between reversing out of place and in place?
4. Which version changes the original list? Which one returns a new list, and which one returns `None`?
5. How do you traverse a list from right to left with `range`? Which indexes does it produce?
6. How do you traverse it backward with negative indexes?
7. In a list of length n, which index is swapped with index i?
8. Why does the in-place version stop at the middle?
9. How many swaps are needed for a list of length n (even and odd)?
10. What happens to the middle item of an odd-length list?
11. What happens if the loop swaps across the whole list instead of stopping at the middle?
12. What happens with an empty list or a one-item list?
13. How would you write the out-of-place version with a while loop instead of a for loop?

## Be able to tell apart

- **for vs while:** a known number of repetitions or every item of a list, or a stopping rule that depends on a changing condition.
- **Condition checks vs body runs:** the condition is checked one more time than the body runs.
- **Zero repetitions vs infinite loop:** the condition is False at the first check, or it never becomes False.
- **Sentinel loop vs retry loop:** stop when the end-of-input value arrives, or ask again while the input is invalid.
- **Priming read vs read at the top of the body:** the check always sees the new value first, or the sentinel gets processed.
- **`if` vs `while` for validation:** checks once, or keeps checking until the input is valid.
- **`and` vs `or` in a validation condition:** "not y and not n" can become False, "not y or not n" never does.
- **Index vs value:** where the match is, or what is stored there.
- **First match vs last match:** the search stops (or is guarded) at the first one, or keeps overwriting the result.
- **Removing with `for` vs `while`:** the index moves on and skips items, or stays put after a removal.
- **Out of place vs in place:** a new list is returned and the original is unchanged, or the original is changed and `None` is returned.

## Not on the quiz

- OOP and Encapsulation.
- Tuples, including tuple packing and unpacking.
- Dictionaries and files.
- `break`, `continue`, `while True:`, and exception handling (`try`/`except`).
- Mutability and aliasing on their own (`notebook.ipynb` Sections 4–5), beyond knowing which reversal changes the original list.
- Writing a full program from scratch (the ElectricCar main program, the 3n+1 program design and pseudocode); only their loop patterns are covered above.
- Built-in shortcuts: `index()`, `count()`, `in` for searching, `reverse()`, `reversed()`, slicing `[::-1]`, `filter()`.
