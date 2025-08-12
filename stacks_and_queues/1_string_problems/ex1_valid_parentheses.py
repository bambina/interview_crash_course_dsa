# Example 1:
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# The string is valid if all open brackets are closed by the same type of closing bracket in the correct order,
# and each closing bracket closes exactly one open bracket.

def valid_parentheses(s: str) -> bool:
  stack = []
  matching = {"(": ")", "[": "]", "{": "}"}

  for c in s:
    if c in matching:
      stack.append(c)
    else:
      if not stack:
        return False
      last_match = stack.pop()
      if matching[last_match] != c:
        return False
  return not stack


test_cases = [
    ("({})", True),
    ("(){}[]", True),
    ("(]", False),
    ("({)}", False),
]

for s, expected in test_cases:
  result = valid_parentheses(s)
  assert result == expected, f"Expected {expected}, got {result}"
