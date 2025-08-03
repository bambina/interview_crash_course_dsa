# Example 2: Given an integer array cards,
# find the length of the shortest subarray that contains at least one duplicate.
# If the array has no duplicates, return -1.

from collections import defaultdict


def shortest_subarray_with_duplicate(cards: list[int]) -> int:
  dic = defaultdict(int)
  ans = float("inf")

  for i in range(len(cards)):
    if cards[i] in dic:
      ans = min(ans, i - dic[cards[i]] + 1)
    dic[cards[i]] = i

  return -1 if ans == float("inf") else ans


test_cases = [
    # Test case 1: Basic case with duplicate
    ([1, 2, 3, 1], 4),

    # Test case 2: No duplicates
    ([1, 2, 3, 4], -1),

    # Test case 3: Adjacent duplicates (shortest possible)
    ([1, 2, 2, 3], 2),

    # Test case 4: Multiple duplicates, return shortest
    ([1, 2, 3, 2, 1], 3),

    # Test case 5: Empty array
    ([], -1)
]

for cards, expected in test_cases:
  result = shortest_subarray_with_duplicate(cards)
  assert result == expected, f"Error: input={cards}, expected={expected}, got={result}"
