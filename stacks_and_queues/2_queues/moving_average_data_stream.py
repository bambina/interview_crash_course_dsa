# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
# Implement the MovingAverage class:
# MovingAverage(int size) Initializes the object with the size of the window size.
# double next(int val) Returns the moving average of the last size values of the stream.

from collections import deque


class MovingAverage:

  def __init__(self, size: int):
    self.queue = deque()
    self.size = size
    self.sum = 0

  def next(self, val: int) -> float:
    self.queue.append(val)
    self.sum += val

    while len(self.queue) > self.size:
      self.sum -= self.queue.popleft()

    return self.sum / len(self.queue)


test_cases = [
    (3, [1, 10, 3, 5], [1.0, 5.5, 4.666666666666667, 6.0]),
    (2, [5, 10, 15, 20], [5.0, 7.5, 12.5, 17.5]),
    (1, [2, 4, 6], [2.0, 4.0, 6.0]),
]

for size, values, expected_results in test_cases:
  ma = MovingAverage(size)
  result = []
  for val in values:
    result.append(ma.next(val))
  assert result == expected_results, f"Expected {expected_results}, got {result}"
