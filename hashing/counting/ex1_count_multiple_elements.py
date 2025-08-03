# Example 1: You are given a string s and an integer k.
# Find the length of the longest substring that contains at most k distinct characters.
# For example, given s = "eceba" and k = 2, return 3.
# The longest substring with at most 2 distinct characters is "ece".

from collections import defaultdict


def find_longest_substring(s: str, k: int) -> int:
  curr = defaultdict(int)
  left = ans = 0
  for right in range(len(s)):
    curr[s[right]] += 1
    while len(curr) > k:
      curr[s[left]] -= 1
      if curr[s[left]] == 0:
        del curr[s[left]]
      left += 1
    ans = max(ans, right-left+1)
  return ans


test_cases = [
    # Given example
    ("eceba", 2, 3),  # "ece" has 2 distinct characters ('e', 'c') and length 3

    # k larger than distinct characters in string
    # entire string "aabbcc" has only 3 distinct chars, so return full length
    ("aabbcc", 5, 6),

    # k = 1, find longest substring with single character
    ("aaabbbccc", 1, 3),  # "aaa", "bbb", or "ccc" each have length 3
]

for s, k, expected in test_cases:
  result = find_longest_substring(s, k)
  assert result == expected, f"Error: s='{s}', k={k}, expected={expected}, got={result}"
