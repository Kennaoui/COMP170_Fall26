# COMP 170: Writing Pseudocode

## Instructions & Template

Formal instructions for any COMP 170 programming assignment. Read this before you start, then use the companion files:

- **`pseudocode-template.py`** - a generic, fill-in-the-blank template you can start any assignment from.
- **`pseudocode-worked-example.py`** - that same shape filled in for a real problem (an investment-plan calculator from Week 3).

## What Pseudocode Is

**Pseudocode** is an English-like description of an algorithm - not a real programming language, but structured enough that it converts easily into one.

Writing pseudocode means thinking a problem through *before* touching Python, so the hard thinking happens on paper, not while you're also fighting syntax errors.

- **Pseudocode comes first.** Writing the code, then describing it afterward, is a different (and much less useful) exercise - and it's graded as if no pseudocode was submitted at all.
- **It's not the same as comments added to finished code.** It's a plan that exists *before* the program does. Once it's solid, a good habit is leaving it in as comments above each function - free documentation, but only after it's done its job as a plan.

## The Process

| Step | What you do |
|---|---|
| **1. Understand the problem** | What's the input and output? What's genuinely difficult about it, and how might you handle that? Restating the prompt is not analysis - identifying what's hard about it is. |
| **2. Decompose** | Break the problem into smaller, named pieces (future functions). Every program needs one function - usually `main` - that coordinates the rest. |
| **3. Describe each piece** | For every function: name, parameters (what each represents), return value (if any), and the essential steps in order. |

## The Key Rule: One Function, One Concern

A function isn't well decomposed just because it has a name. The real test:

> Can you describe its job in one sentence, without joining two unrelated actions with "and"?

"Reads the input *and* calculates *and* prints it" is three jobs wearing one name. These are separate concerns and belong in separate functions. Keeping these apart is what makes a function reusable: a calculation that only calculates can be tested or reused anywhere, while one tangled up with input/output is stuck serving only its original spot.

Watch both extremes:

- **Too coarse** - one function doing everything. This is the most common problem, and the one graded most strictly.
- **Too fine** - splitting one indivisible step into functions for no real reason.

Decompose along the problem's natural seams, not to hit a function count. A well-decomposed program is typically small "worker" functions (each doing exactly one of read/calculate/display) plus one coordinating function that calls them in order.

## Grading Rubric

These deductions apply to any COMP 170 programming assignment that includes a pseudocode component, expressed as a percentage of that assignment's total points (since point totals vary by assignment).

| Category | Deduction | What it covers |
|---|---|---|
| **Decomposition into functions** | up to 25% | No meaningful breakup of the problem into functions, or it's unclear what functions are planned. |
| **Redundancy** | 10% to 20% | Code or pseudocode repeated in more than one place in exactly or nearly the same form. |
| **Problem analysis** | 5% to 20% | Incomplete analysis of the problem, depending on severity. Restating the prompt is not analysis - analysis means identifying what's genuinely hard about the problem and sketching an approach. A submission with no real analysis at all falls at the top of this range. |
| **Pseudocode format** | 30% | Code only, with no pseudocode at all. |
