# Example 3: Given two sorted integer arrays arr1 and arr2,
# return a new array that combines both of them and is also sorted.

def combine(arr1: list[int], arr2: list[int]) -> list[int]:
  i = j = 0
  result = []
  while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
      result.append(arr1[i])
      i += 1
    else:
      result.append(arr2[j])
      j += 1

  while i < len(arr1):
    result.append(arr1[i])
    i += 1

  while j < len(arr2):
    result.append(arr2[j])
    j += 1

  return result


test_cases = [
    ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),        # equal length arrays
    ([1, 2, 3], [4, 5], [1, 2, 3, 4, 5]),              # arr1 longer than arr2
    ([5, 6], [1, 2, 3, 4], [1, 2, 3, 4, 5, 6]),        # arr2 longer than arr1
]

for arr1, arr2, expected in test_cases:
  result = combine(arr1, arr2)
  assert result == expected, "Error"
