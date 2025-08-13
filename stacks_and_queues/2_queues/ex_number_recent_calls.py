# Example:
# Implement the RecentCounter class .
# It should support ping(int t), which records a call at time t,
# and then returns an integer representing the number of calls that have happened in the range[t - 3000, t].
# Calls to ping will have increasing t.

from collections import deque


class RecentCounter:
  def __init__(self):
    self.queue = deque()

  def ping(self, t: int) -> int:
    while self.queue and self.queue[0] < t-3000:
      self.queue.popleft()
    self.queue.append(t)
    return len(self.queue)


test_cases = [
    ([1, 100, 3001, 3002], [1, 2, 3, 3]),
    ([1, 100, 3001, 4000], [1, 2, 3, 2]),
    ([1, 1000, 2000, 3000], [1, 2, 3, 4]),
]

for calls, expected_results in test_cases:
  counter = RecentCounter()
  result = []
  for t in calls:
    result.append(counter.ping(t))
  assert result == expected_results, f"Expected {expected_results}, got {result}"
