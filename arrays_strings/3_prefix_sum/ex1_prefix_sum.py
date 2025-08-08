# Example 1: Given an integer array nums,
# an array queries where queries[i] = [x, y] and an integer limit,
# return a boolean array that represents the answer to each query.
# A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.

# For example, given nums = [1, 6, 3, 2, 7, 2],
# queries = [[0, 3], [2, 5], [2, 4]], and limit = 13,
# the answer is [true, false, true]. For each query, the subarray sums are [12, 14, 12].

def answer_queries(nums: list[int], queries: list[list[int]], limit: int) -> list[bool]:
  prefix = [nums[0]]
  for i in range(1, len(nums)):
    prefix.append(nums[i] + prefix[-1])

  res = []
  for x, y in queries:
    sum_subarray = prefix[y] - prefix[x] + nums[x]
    res.append(sum_subarray < limit)

  return res


test_cases = [
    # Given example
    ([1, 6, 3, 2, 7, 2], [[0, 3], [2, 5], [2, 4]], 13, [True, False, True]),
    # nums[0:3] = 1+6+3+2 = 12 < 13 → True
    # nums[2:5] = 3+2+7+2 = 14 >= 13 → False
    # nums[2:4] = 3+2+7 = 12 < 13 → True

    # All queries return False (sums exceed limit)
    ([5, 10, 15, 20], [[0, 1], [1, 3]], 10, [False, False]),
    # nums[0:1] = 5+10 = 15 >= 10 → False
    # nums[1:3] = 10+15+20 = 45 >= 10 → False

    # Single element queries
    ([2, 8, 4, 6], [[0, 0], [1, 1], [3, 3]], 5, [True, False, False])
    # nums[0:0] = 2 < 5 → True
    # nums[1:1] = 8 >= 5 → False
    # nums[3:3] = 6 >= 5 → False
]

for nums, queries, limit, expected in test_cases:
  result = answer_queries(nums, queries, limit)
  assert result == expected, f"Expected {expected}, got {result}"
