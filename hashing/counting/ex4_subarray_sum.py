# Example 4:
# Given an integer array nums and an integer k,
# find the number of subarrays whose sum is equal to k.

from collections import defaultdict


def subarray_sum(nums: list[int], k: int) -> int:
  curr = ans = 0
  counts = defaultdict(int)
  counts[0] = 1

  for i in range(len(nums)):
    curr += nums[i]
    ans += counts[curr-k]
    counts[curr] += 1

  return ans


test_cases = [
    # Basic case with positive numbers
    ([1, 1, 1], 2, 2),  # subarrays: [1,1] at index 0-1, and [1,1] at index 1-2

    # Array with negative numbers and zero
    ([1, 2, 3], 3, 2),  # subarrays: [3] at index 2, and [1,2] at index 0-1

    ([1, 2, 1, 2, 1], 3, 4),
]

for nums, k, expected in test_cases:
  result = subarray_sum(nums, k)
  assert result == expected, f"Error: nums={nums}, k={k}, expected={expected}, got={result}"
