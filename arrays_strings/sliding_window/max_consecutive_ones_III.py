# Given a binary array nums and an integer k,
# return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

def find_max_consecutive_ones(nums: list[int], k: int) -> int:
  curr = max_len = right = left = 0
  while right < len(nums):
    if nums[right] == 0:
      curr += 1
    while curr > k:
      if nums[left] == 0:
        curr -= 1
      left += 1
    max_len = max(max_len, right-left+1)
    right += 1
  return max_len


test_cases = [
    ([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2, 6),
    ([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3, 10),
    ([1, 0, 1, 1, 0], 0, 2),
]

for nums, k, expected in test_cases:
  result = find_max_consecutive_ones(nums, k)
  assert result == expected, f"Expected {expected}, got {result}"
