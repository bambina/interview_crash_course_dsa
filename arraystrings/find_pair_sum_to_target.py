# Example 2: Given a sorted array of unique integers and a target integer,
# return true if there exists a pair of numbers that sum to target, false otherwise.

def check_for_target(nums: list[int], target: int) -> bool:
  small = 0
  large = len(nums) - 1
  while small < large:
    sum = nums[small] + nums[large]
    if sum == target:
      # print(f"Found: small is {nums[small]}(idx={small}) and large is {nums[large]}(idx={large})")
      return True

    if sum > target:
      large -= 1
    else:
      small += 1

  return False


test_cases = [
    ([1, 2, 4, 6, 8, 9, 14, 15], 13, True),     # original case: 6 + 7 = 13
    ([1, 2, 4, 6, 8, 9, 14, 15], 3, True),      # small numbers: 1 + 2 = 3
    ([1, 2, 4, 6, 8, 9, 14, 15], 29, True),     # large numbers: 14 + 15 = 29
    ([1, 2, 4, 6, 8, 9, 14, 15], 100, False),   # target too large
    ([1, 2, 4, 6, 8, 9, 14, 15], 1, False),     # target too small
    ([5], 5, False),                            # single element
    ([], 10, False),                            # empty array
    ([1, 2, 3, 4, 5], 9, True),                 # last two: 4 + 5 = 9
    ([1, 2, 3, 4, 5], 3, True),                 # first two: 1 + 2 = 3
]

for nums, target, expected in test_cases:
  result = check_for_target(nums, target)
  assert result == expected, f"Failed for nums={nums}, target={target}: got {result}, expected {expected}"
