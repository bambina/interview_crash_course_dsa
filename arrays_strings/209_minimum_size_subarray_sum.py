# Given an array of positive integers nums and a positive integer target,
# return the minimal length of a subarray whose sum is greater than or equal to target.
# If there is no such subarray, return 0 instead.

def minSubArrayLen(target: int, nums: list[int]) -> int:
  left = right = curr = 0
  ans = float('inf')
  while right < len(nums):
    curr += nums[right]
    while curr >= target:
      ans = min(ans, right-left+1)
      curr -= nums[left]
      left += 1
    right += 1
  return 0 if ans == float('inf') else ans


test_cases = [
    (7, [2, 3, 1, 2, 4, 3], 2),
    (4, [1, 4, 4], 1),
    (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),
]

for target, nums, expected in test_cases:
  res = minSubArrayLen(target, nums)
  assert res == expected, f"Expected {expected}, got {res}"
