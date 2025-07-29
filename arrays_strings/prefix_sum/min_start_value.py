# Given an array of integers nums, you start with an initial positive value startValue.
# In each iteration, you calculate the step by step sum of startValue plus elements in nums(from left to right).
# Return the minimum positive value of startValue such that the step by step sum is never less than 1.

def min_start_value(nums: list[int]) -> int:
  min_val = sum = nums[0]
  for i in range(1, len(nums)):
    sum += nums[i]
    min_val = min(min_val, sum)

  return max(1, 1-min_val)


test_cases = [
    ([-3, 2, -3, 4, 2], 5),
    ([1, 2], 1),
    ([1, -2, -3], 5),
]

for nums, expected in test_cases:
  result = min_start_value(nums)
  assert result == expected, f"Expected {expected}, got {result}"
