# You are given a 0-indexed array nums of n integers, and an integer k.
# The k-radius average for a subarray of nums centered at some index i with the radius k is the average of all elements in nums between the indices i - k and i + k(inclusive).
# If there are less than k elements before or after the index i, then the k-radius average is -1.
# Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.

# The integer division truncates toward zero, which means losing its fractional part.

def get_averages(nums: list[int], k: int) -> list[int]:
  n = len(nums)
  ans = [-1]*n
  subarr_len = 2*k+1
  if len(nums) < subarr_len:
    return ans

  curr = 0
  for i in range(n):
    curr += nums[i]
    start = i-subarr_len+1
    if start >= 0:
      ans[i-k] = curr // subarr_len
      curr -= nums[start]

  return ans


test_cases = [
    ([7, 4, 3, 9, 1, 8, 5, 2, 6], 3, [-1, -1, -1, 5, 4, 4, -1, -1, -1]),
    ([100000], 0, [100000]),
    ([8], 100000, [-1]),
]

for nums, k, expected in test_cases:
  result = get_averages(nums, k)
  assert result == expected, f"Expected {expected}, got {result}"
