# Example 2:
# Given a 2D array nums that contains n arrays of distinct integers,
# return a sorted array containing all the numbers that appear in all n arrays.

# For example, given nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]],
# return [3, 4]. 3 and 4 are the only numbers that are in all arrays.

from collections import defaultdict


def intersection(nums: list[list[int]]) -> list[int]:
  count = defaultdict(int)
  for arr in nums:
    for elem in arr:
      count[elem] += 1

  n = len(nums)
  ans = []
  for k, v in count.items():
    if v == n:
      ans.append(k)

  return sorted(ans)


test_cases = [
    # Given example
    ([[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]], [3, 4]),
    # 3 and 4 appear in all three arrays

    # No common elements
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], []),
    # No numbers appear in all arrays
]

for nums, expected in test_cases:
  result = intersection(nums)
  assert result == expected, f"Error: nums={nums}, expected={expected}, got={result}"
