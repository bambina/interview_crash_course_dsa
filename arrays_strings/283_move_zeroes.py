# Given an integer array nums,
# move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.


def move_zeroes(nums: list[int]):
  non_zero = 0
  for i in range(len(nums)):
    if nums[i] != 0:
      nums[non_zero], nums[i] = nums[i], nums[non_zero]
      non_zero += 1


test_cases = [
    ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
    ([0, 0, 1], [1, 0, 0]),
    ([1, 2, 3], [1, 2, 3]),
]

for nums, expected in test_cases:
  move_zeroes(nums)
  assert nums == expected, f"Expected {expected}, got {nums}"
