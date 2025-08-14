# Example 2:
# Given an integer array nums and an integer k,
# there is a sliding window of size k that moves from the very left to the very right.
# For each window, find the maximum element in the window.
# For example, given nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3, return [3, 3, 5, 5, 6, 7].
# The first window is [1, 3, -1, -3, 5, 3, 6, 7] and the last window is [1, 3, -1, -3, 5, 3, 6, 7]

from collections import deque


def max_sliding_window(nums: list[int], k: int) -> list[int]:
  ans = []
  queue = deque()
  for i in range(len(nums)):
    while queue and nums[queue[-1]] < nums[i]:
      queue.pop()
    queue.append(i)

    # [0, 1, 2, 3]
    if queue[0] + k == i:
      queue.popleft()

    if i >= k-1:
      ans.append(nums[queue[0]])

  return ans


test_cases = [
    ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
    ([1, -1, -3, 5, 3, 6, 7], 1, [1, -1, -3, 5, 3, 6, 7]),
]

for nums, k, expected in test_cases:
  result = max_sliding_window(nums, k)
  assert result == expected, f"Expected {expected}, got {result}"
