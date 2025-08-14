# Example 1:
# Given an array of integers temperatures that represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have to wait
# after the ith day to get a warmer temperature.
# If there is no future day that is warmer, have answer[i] = 0 instead.

def daily_temperatures(temperatures: list[int]) -> list[int]:
  stack = []
  ans = [0] * len(temperatures)
  for i in range(len(temperatures)):
    while stack and temperatures[stack[-1]] < temperatures[i]:
      j = stack.pop()
      ans[j] = i-j
    stack.append(i)
  return ans


test_cases = [
    ([40, 35, 32, 37, 50], [4, 2, 1, 1, 0]),
    ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
]

for temperatures, expected in test_cases:
  result = daily_temperatures(temperatures)
  assert result == expected, f"Expected {expected}, got {result}"
