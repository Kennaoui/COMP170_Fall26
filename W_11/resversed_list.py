def reverse_out_of_place(items: list[int]) -> list[int]:
  result = []
  for i in range(-1, -len(items) - 1, -1):
    result.append(items[i])
  return result

def swap(items: list[int], i: int, j: int) -> None:
  pass
