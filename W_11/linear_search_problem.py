def first_passing_score_for(scores: list[int]) -> int:
    """Return the first passing index; for loop visits every element."""
    first_index = -1
    for i in range(len(scores)):
        if first_index == -1 and scores[i] >= 7:
            first_index = i
    return first_index


def first_passing_score(scores: list[int]) -> int:
    """Return the index of the first score >= 7, or -1 if absent."""
    i = 0
    while i < len(scores) and scores[i] < 7:
        i += 1
    if i == len(scores):
        return -1
    return i
