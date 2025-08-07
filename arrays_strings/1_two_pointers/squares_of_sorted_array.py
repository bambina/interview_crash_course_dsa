# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.

def squares_of_sorted_array(nums: list[int]) -> list[int]:
  i = 0
  j = end_idx = len(nums) - 1
  res = [0] * len(nums)

  while end_idx > -1:
    if abs(nums[i]) > abs(nums[j]):
      res[end_idx] = nums[i] ** 2
      i += 1
    else:
      res[end_idx] = nums[j] ** 2
      j -= 1
    end_idx -= 1

  return res


test_cases = [
    ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
    ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121])
]

for nums, expected in test_cases:
  result = squares_of_sorted_array(nums)
  assert result == expected, "Error"
