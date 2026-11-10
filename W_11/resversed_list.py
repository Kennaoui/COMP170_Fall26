
# Reverse list out of place
def reverse_out_of_place(items: list[int]) -> list[int]:
  """ Take as input is a list of integers, and output a diffrent list of integers that has all elements of items but in reverse order.  """
  result = []
  for i in range(-1, -len(items) - 1, -1):
    result.append(items[i])
  return result

# Swapping two values in a list
def swap(items: list[int], i: int, j: int) -> None:
  pass

# Reverse list in place
def reverse_in_place(items: list[int]) -> None:
  pass
