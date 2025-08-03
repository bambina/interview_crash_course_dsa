# Example 3: Given an integer array nums, find all the numbers x in nums
# that satisfy the following: x + 1 is not in nums, and x - 1 is not in nums.
# If a valid number x appears multiple times,
# you only need to include it in the answer once.

def find_numbers(nums: list[int]) -> list[int]:
  ans = []
  nums_set = set(nums)
  for n in nums_set:
    if (n+1) not in nums_set and (n-1) not in nums_set:
      ans.append(n)
  return ans


test_cases = [
    # 5 and 8 have no adjacent numbers (4,6 and 7,9 not in array)
    ([1, 2, 3, 5, 8], [5, 8]),

    # None of these have adjacent numbers in the array
    ([10, 15, 20], [10, 15, 20]),

    # No isolated numbers (all consecutive)
    ([1, 2, 3, 4, 5], [])
]

for nums, expected in test_cases:
  result = find_numbers(nums)
  # Sort both lists for comparison since order may vary
  assert sorted(result) == sorted(
      expected), f"Error: nums={nums}, expected={expected}, got={result}"
