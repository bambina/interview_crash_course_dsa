# Example 2:
# You are given a string s.
# Continuously remove duplicates(two of the same character beside each other)
# until you can't anymore. Return the final string after this.

def remove_adjacent_duplicates(s: str) -> str:
  stack = []
  for c in s:
    if stack and stack[-1] == c:
      stack.pop()
    else:
      stack.append(c)

  return "".join(stack)


test_cases = [
    ("abbaca", "ca"),
    ("abccba", ""),
    ("azxxzy", "ay"),
    ("aabbcc", ""),
]

for s, expected in test_cases:
  result = remove_adjacent_duplicates(s)
  assert result == expected, f"Expected {expected}, got {result}"
