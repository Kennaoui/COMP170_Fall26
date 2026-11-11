def first_passing_score_for_V1(scores: list[int]) -> int:
    """Return the first passing index; for loop visits every element."""
    first_index = -1
    for i in range(len(scores)):
        if scores[i] >= 7 and first_index == -1:
            first_index = i
    return first_index

def first_passing_score_for_V2(scores: list[int]) -> int:
    """Return the first passing grade index; for loop stops early when the first passing grade is found."""
    first_index = -1
    for i in range(len(scores)):
        if scores[i] >= 7:
            first_index = i
            break
    return first_index


def first_passing_score_for_V3(scores: list[int]) -> int:
    """Return the first passing grade index; for loop stops early when the first passing grade is found"""
    no_p_score = -1
    for i in range(len(scores)):
        if scores[i] >= 7:
            return i
    return no_p_score


def first_passing_score_while(scores: list[int]) -> int:
    """Return the index of the first score >= 7, or -1 if absent. Stop early."""
    first_index = -1
    i = 0
    while i < len(scores) and first_p_score == -1:
        if score[i] >= 7:
           first_index = i
        i += 1
        
    return first_index
