# Example 3:
# Given a string s, determine if all characters have the same frequency.

# For example, given s = "abacbc", return true, because all characters appear twice.
# Given s = "aaabb", return false. "a" appears 3 times, "b" appears 2 times. 3 != 2.
from collections import defaultdict


def are_occurrences_equal(s: str) -> bool:
  counts = defaultdict(int)
  for c in s:
    counts[c] += 1

  return len(set(counts.values())) == 1


test_cases = [
    # All characters have same frequency
    ("abacbc", True),  # 'a':2, 'b':2, 'c':2 - all appear twice

    # Characters have different frequencies
    ("aaabb", False),  # 'a':3, 'b':2 - different frequencies
]

for s, expected in test_cases:
  result = are_occurrences_equal(s)
  assert result == expected, f"Error: s='{s}', expected={expected}, got={result}"
