# Example 4: Given an integer array nums and an integer k,
# find the sum of the subarray with the largest sum whose length is k.

def largest_sum_subarray(nums: list[int], k: int) -> int:
  curr = 0
  for i in range(k):
    curr += nums[i]

  ans = curr
  for i in range(k, len(nums)):
    curr += nums[i] - nums[i-k]
    ans = max(ans, curr)

  return ans


test_cases = [
    ([1, 2, 3, 4, 5], 3, 12),
    ([-1, 2, -3, 4, 5], 2, 9),
    ([-5, -2, -8, -1], 2, -7),
    ([1, -2, 3, -4, 5], 5, 3),
]

for nums, k, expected in test_cases:
  result = largest_sum_subarray(nums, k)
  assert result == expected, f"Error: nums={nums}, k={k}, expected={expected}, got={result}"
