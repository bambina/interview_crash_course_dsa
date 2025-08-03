# Example 2:
# Given a string s, return the first character to appear twice.
# It is guaranteed that the input will have a duplicate character.

def repeated_char(s: str) -> str:
  seen = set()
  for c in s:
    if c in seen:
      return c
    seen.add(c)
  return ""


test_cases = [
    ("abccba", "c"),  # 'c' appears at index 2 and 3, first to repeat
    ("aabcd", "a"),  # 'a' appears at index 0 and 1, first to repeat
    ("abcdef", "")
]

for s, expected in test_cases:
  result = repeated_char(s)
  assert result == expected, f"Error: s='{s}', expected='{expected}', got='{result}'"
