
# Reverse list out of place
# Version 1: Using negative indices
def reverse_copy_V1(items: list[int]) -> list[int]:
  """ Take as input is a list of integers, and output a copy in reverse order.  """
  result = []
  for i in range(-1, -len(items) - 1, -1):
    result.append(items[i])
  return result

# Version 2: Using positive indices
def reversed_copy_V2(items: list[int]) -> list[int]:
    """ Take as input is a list of integers, and output a copy in reverse order.  """
    result = []
    for i in range(len(items) - 1, -1, -1):
        result.append(items[i])
    return result


# Swapping two values in a list
def swap(items: list[int], i: int, j: int) -> None:
  """ Swap the values in items[i] and items[j]"""
  pass

# Reverse list in place
def reverse_in_place(items: list[int]) -> None:
  pass
