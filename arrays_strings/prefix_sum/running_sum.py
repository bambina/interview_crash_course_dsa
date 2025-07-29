# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

def running_sum(nums: list[int]) -> list[int]:
  prefix = [nums[0]]
  for i in range(1, len(nums)):
    prefix.append(nums[i]+prefix[-1])
  return prefix


test_cases = [
    ([1, 2, 3, 4], [1, 3, 6, 10]),
    ([1, 1, 1, 1, 1], [1, 2, 3, 4, 5]),
    ([3, 1, 2, 10, 1], [3, 4, 6, 16, 17]),
]

for nums, expected in test_cases:
  result = running_sum(nums)
  assert result == expected, f"Expected {expected}, got {result}"
