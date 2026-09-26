from math import sqrt, ceil

def side_length(area: float) -> float:
    """Return the side length of a square with the given area."""
    return sqrt(area)


def whole_side_length(area: float) -> int:
    """Return the biggest whole-number side length that is large enough."""
    return ceil(side_length(area))

print("Testing:", whole_side_length(20))
