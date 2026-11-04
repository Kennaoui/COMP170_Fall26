def first_passing_score_for(scores: list[int]) -> int:
    """Return the first passing index; for loop visits every element."""
    no_p_score = -1
    for i in range(len(scores)):
        if scores[i] >= 7:
            return i
    return no_p_score


def first_passing_score(scores: list[int]) -> int:
    """Return the index of the first score >= 7, or -1 if absent."""
    first_p_score = -1
    i = 0
    while i < len(scores) and first_p_score == -1:
        if score[i] >= 7:
           first_p_score = i
        i += 1
        
    return first_p_score
