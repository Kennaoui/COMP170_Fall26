# Using type() — INCORRECT
# input() always returns a string, so type() cannot validate numeric input.
# This loop never terminates.

def get_quiz_score_v1() -> int:
    score = int(input("Enter a score (0-10): "))

    while type(score) != int or int(score) < 0 or int(score) > 10:
        print("Invalid score. Try again.")
        score = int(input("Enter a score (0-10): "))

    return score


# Using isdigit() — ACCEPTABLE
# Works for simple inputs, but checks characters rather than conversion.
# For example, it rejects "+5" and " 5 ", although both are valid integers.

def get_quiz_score_v2() -> int:
    score = input("Enter a score (0-10): ")

    while not (score.isdigit() and 0 <= int(score) <= 10):
        print("Invalid score. Try again.")
        score = input("Enter a score (0-10): ")

    return int(score)


# Using while True — NOT ACCEPTABLE AT THIS STAGE
# Although valid Python, it hides the stopping condition inside the loop.
# We should practice expressing that condition directly in the while statement.

def get_quiz_score_v3() -> int:
    while True:
        score = input("Enter a score (0-10): ")

        if score.isdigit() and 0 <= int(score) <= 10:
            return int(score)

        print("Invalid score. Try again.")


# Using try/except — Good
# More flexible: attempts the actual conversion and handles errors.
# Separates conversion errors from range validation.
# Uses a priming read and an explicit while condition.

def get_quiz_score_v4() -> int:
    score = input("Enter a score (0-10): ")

    try:
        score = int(score)
    except ValueError:
        score = -1

    while score < 0 or score > 10:
        print("Invalid score. Try again.")
        score = input("Enter a score (0-10): ")

        try:
            score = int(score)
        except ValueError:
            score = -1

    return score

# Using a helper function with try/except — RECOMMENDED
# Clean and reusable: separates input validation from the while loop.
# Avoids repeating the try/except block and keeps the stopping condition clear.
# A good use of functions, exception handling, and priming reads.

def valid_score(score: str) -> bool:
    try:
        number = int(score)
        return 0 <= number <= 10
    except ValueError:
        return False


def get_quiz_score() -> int:
    score = input("Enter a quiz score (0-10): ")

    while not valid_score(score):
        print("Invalid score. Try again.")
        score = input("Enter a quiz score (0-10): ")

    return int(score)
