# Example 1: Given an array of positive integers nums and an integer k,
# find the length of the longest subarray whose sum is less than or equal to k.

def find_length(nums: list[int], k: int) -> int:
  left = curr_sum = res = 0

  for right in range(len(nums)):
    curr_sum += nums[right]
    while curr_sum > k:
      curr_sum -= nums[left]
      left += 1
    res = max(res, right-left+1)

  return res


test_cases = [
    # subarray [1, 2, 1, 1] has sum 5 ≤ 8, length = 4
    ([3, 1, 2, 7, 4, 2, 1, 1, 5], 8, 4),
    # subarray [1, 2, 3, 4] has sum 10 ≤ 11, length = 4
    ([1, 2, 3, 4, 5], 11, 4),
]

for nums, k, expected in test_cases:
  result = find_length(nums, k)
  assert result == expected, f"Error: nums={nums}, k={k}, got {result}, expected {expected}"
