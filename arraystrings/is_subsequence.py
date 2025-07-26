# Example 4: Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

def is_subsequence(s: list[str], t: list[str]) -> bool:
  i = j = 0
  while i < len(s) and j < len(t):
    if s[i] == t[j]:
      i += 1
    j += 1
  return i == len(s)


test_cases = [
    (list("ace"), list("abcde"), True),        # typical subsequence case
    (list("aec"), list("abcde"), False),       # wrong order, not a subsequence
    (list("abc"), list("aabbcc"), True),       # duplicates in t, still valid
    # empty s is always a subsequence
    (list(""), list("abc"), True),
]

for s, t, expected in test_cases:
  result = is_subsequence(s, t)
  assert result == expected, "Error"
