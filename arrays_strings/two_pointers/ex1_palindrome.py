# Example 1: Given a string s, return true if it is a palindrome, false otherwise.

def check_if_palindrome(s: list[str]) -> bool:
  i = 0
  j = len(s) - 1
  while i < j:
    if s[i] != s[j]:
      return False
    i += 1
    j -= 1
  return True


test_cases = [
    ("abcdcba", True),      # odd-length palindrome
    ("computer", False),    # not a palindrome
    ("abccba", True),       # even-length palindrome
    ("a", True),            # single character (palindrome)
    ("ab", False),          # two characters (not palindrome)
    ("aa", True),           # two characters (palindrome)
    ("", True),             # empty string (considered palindrome)
]

for case, expected in test_cases:
  result = check_if_palindrome(list(case))
  assert result == expected, f"Failed for '{case}': got {result}, expected {expected}"
