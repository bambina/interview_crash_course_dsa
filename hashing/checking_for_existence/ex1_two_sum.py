# Example 1: Given an array of integers nums and an integer target,
# return indices of two numbers such that they add up to target.
# You cannot use the same index twice.

def two_sum(nums: list[int], target: int) -> set[int]:
  dic = {}
  for i in range(len(nums)):
    num = nums[i]
    complement = target - num
    if complement in dic:
      return {i, dic[complement]}
    dic[num] = i
  return {-1}


test_cases = [
    ([2, 7, 11, 15], 9, {0, 1}),  # nums[0] + nums[1] = 2 + 7 = 9
    ([3, 2, 4], 6, {1, 2}),  # nums[1] + nums[2] = 2 + 4 = 6
    ([1, 2, 3], 10, {-1})  # No two numbers add up to 10
]

for nums, target, expected in test_cases:
  result = two_sum(nums, target)
  assert result == expected, f"Error: nums={nums}, target={target}, expected={expected}, got={result}"
