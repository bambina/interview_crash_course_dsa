# Example 3:
# Given two strings s and t, return true if they are equal when both are typed into empty text editors.
# '#' means a backspace character.
#
# For example, given s = "ab#c" and t = "ad#c", return true.
# Because of the backspace, the strings are both equal to "ac".

def backspace_string_compare(s: str, t: str) -> bool:
  def build(s: str) -> str:
    stack = []
    for c in s:
      if c != "#":
        stack.append(c)
      elif stack:
        stack.pop()
    return "".join(stack)

  return build(s) == build(t)


test_cases = [
    ("ab#c", "ad#c", True),
    ("ab##", "c#d#", True),
    ("a##c", "#a#c", True),
]

for s, t, expected in test_cases:
  result = backspace_string_compare(s, t)
  assert result == expected, f"Expected {expected}, got {result}"
