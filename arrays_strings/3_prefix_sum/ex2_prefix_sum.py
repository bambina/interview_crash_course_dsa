# Example 2: Given an integer array nums,
# find the number of ways to split the array into two parts
# so that the first section has a sum greater than or equal to the sum of the second section.
# The second section should have at least one number.

def ways_to_split_array(nums: list[int]) -> int:
  total_sum = sum(nums)
  left = res = 0
  for i in range(len(nums)-1):
    left += nums[i]
    right = total_sum - left
    if left >= right:
      res += 1
  return res

# def ways_to_split_array(nums: list[int]) -> int:
#   prefix = [nums[0]]
#   for i in range(1, len(nums)):
#     prefix.append(nums[i] + prefix[-1])

#   res = 0
#   for i in range(len(nums)-1):
#     left = prefix[i]
#     right = prefix[-1] - prefix[i]
#     if left >= right:
#       res += 1
#   return res


test_cases = [
    ([10, 4, -8, 7], 2),
    # Split at index 0: [10] vs [4, -8, 7] → 10 >= 3 ✓
    # Split at index 1: [10, 4] vs [-8, 7] → 14 >= -1 ✓
    # Split at index 2: [10, 4, -8] vs [7] → 6 < 7 ✗

    ([2, 3, 1, 0], 2),
    # Split at index 0: [2] vs [3, 1, 0] → 2 < 4 ✗
    # Split at index 1: [2, 3] vs [1, 0] → 5 >= 1 ✓
    # Split at index 2: [2, 3, 1] vs [0] → 6 >= 0 ✓

    ([2, 3, 1, 6], 1)
    # Split at index 0: [2] vs [3, 1, 6] → 2 < 10 ✗
    # Split at index 1: [2, 3] vs [1, 6] → 5 < 7 ✗
    # Split at index 2: [2, 3, 1] vs [6] → 6 >= 6 ✓
]

for nums, expected in test_cases:
  result = ways_to_split_array(nums)
  assert result == expected, f"Expected {expected}, got {result}"
