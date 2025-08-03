# Example 3:
# Given an array of integers nums, find the maximum value of nums[i] + nums[j],
# where nums[i] and nums[j] have the same digit sum(the sum of their individual digits).
# Return - 1 if there is no pair of numbers with the same digit sum.
from collections import defaultdict


def max_sum_same_digit_sum(nums: list[int]) -> int:
  def get_digit_sum(num: int) -> int:
    digit_sum = 0
    while num:
      digit_sum += num % 10
      num //= 10
    return digit_sum

  ans = -1
  hm = defaultdict(int)
  for i in range(len(nums)):
    digit_sum = get_digit_sum(nums[i])
    if digit_sum in hm:
      ans = max(ans, nums[i]+hm[digit_sum])
    hm[digit_sum] = max(hm[digit_sum], nums[i])
  return ans


test_cases = [
    # Test case 1: Basic case with same digit sum
    ([18, 43, 36, 13, 7], 54),  # 18(1+8=9) + 36(3+6=9) = 54

    # Test case 2: No pairs with same digit sum
    ([10, 12, 19, 14], -1),  # digit sums: 1, 3, 10, 5 (all different)

    # Test case 3: Multiple pairs, find maximum
    # 51(5+1=6) + 42(4+2=6) = 93, 71(7+1=8) + 17(1+7=8) = 88, max is 93
    ([51, 71, 17, 42], 93),
]

for nums, expected in test_cases:
  result = max_sum_same_digit_sum(nums)
  assert result == expected, f"Error: input={nums}, expected={expected}, got={result}"
