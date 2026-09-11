# COMP 170 -- Generic Pseudocode Template
# This is the fill-in-the-blank shape to use for ANY pseudocode
# assignment. It is not tied to one specific problem -- replace every
# <...> placeholder with whatever fits the problem you're actually
# solving. For a worked example showing this shape filled in for a
# real problem, see pseudocode-worked-example.py.
#
# See pseudocode-instructions.md for the full explanation of each part
# of this template and why it's shaped this way.

# COMP 170 Standard Python Header
# Assignment: <assignment name>
# Name and Loyola Id/email: <your name and Loyola ID or email>
# Date: <date>
#
# DESCRIPTION: <one or two sentences describing what the program does,
# from the user's point of view>
#
# QUESTIONS: <anything you're unsure about, or "None">
#
# PROBLEM ANALYSIS & KEY ISSUES:
# <what's genuinely hard about this problem, and your idea for handling
# it -- not a restatement of the assignment>
#
# PROGRAM PSEUDOCODE:
# <state the overall workflow of the program, in order -- what happens
# first, next, and so on, and which function handles each step. usually starts with the main.>
#
# FUNCTIONS:
# <one line per function you're planning: its name, and the one job
# it's responsible for. Every program needs a main function that
# coordinates the rest -- add as many other functions as your own
# decomposition needs.>


# One generic example of how to introduce a function: a signature with
# type annotations, followed by a docstring covering its purpose,
# inputs, return value, and any constraints the annotations don't
# capture. Repeat this pattern for every function your own
# decomposition needs.
def function_name(parameter_name: "parameter type") -> "return type":
    """
    <One sentence: the single job this function does.>
    Takes as input parameter_name: <what it represents, plus any
    constraint the type alone doesn't capture -- e.g., "must be a
    positive whole number.">
    Return <what's returned, plus any constraint>.
    <The essential steps, in order, if they aren't obvious from the
    above.>
    """
    # <function body goes here, once the pseudocode above is solid>


def main():
    # Call the function(s) above, in the order described in
    # PROGRAM PSEUDOCODE.
    pass


main()
