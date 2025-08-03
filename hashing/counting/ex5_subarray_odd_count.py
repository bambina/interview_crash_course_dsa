# Example 5:
# Given an array of positive integers nums and an integer k.
# Find the number of subarrays with exactly k odd numbers in them.


from collections import defaultdict


def subarray_odd_count(nums: list[int], k: int) -> int:
  ans = curr = 0
  counts = defaultdict(int)
  counts[0] = 1
  for num in nums:
    curr += num % 2
    ans += counts[curr-k]
    counts[curr] += 1

  return ans


test_cases = [
    ([1, 1, 2, 1, 1], 3, 2),
    ([2, 1, 2, 2], 1, 6),
    ([2, 4, 3, 6], 0, 4),
]

for nums, k, expected in test_cases:
  result = subarray_odd_count(nums, k)
  assert result == expected, f"Error: nums={nums}, k={k}, expected={expected}, got={result}"
