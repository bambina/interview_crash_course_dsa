# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.

def find_max_average(nums: list[int], k: int) -> float:
  curr = sum(nums[:k])
  max_sum = curr

  for i in range(k, len(nums)):
    curr += nums[i] - nums[i-k]
    max_sum = max(max_sum, curr)

  return max_sum / k


test_cases = [
    ([1, 12, -5, -6, 50, 3], 4, 12.75000),
    ([1, 2, 3, 4, 5], 3, 4.0),  # subarray [3, 4, 5] = 12/3 = 4.0
    ([-1, -2, -3, -4, -5], 2, -1.5),  # subarray [-1, -2] = -3/2 = -1.5
    ([5, 10, 15], 3, 10.0),  # entire array = 30/3 = 10.0
    ([10, -5, 3, 8], 1, 10.0),  # maximum single element = 10.0
]

for nums, k, expected in test_cases:
  result = find_max_average(nums, k)
  assert abs(result - expected) < 1e-5, f"Expected {expected}, got {result}"
