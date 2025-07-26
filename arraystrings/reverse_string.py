# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in -place with O(1) extra memory.

def reverse_string(s: list[str]) -> None:
  i = 0
  j = len(s) - 1

  while i < j:
    s[i], s[j] = s[j], s[i]
    i += 1
    j -= 1


test_cases = [
    (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),  # odd length
    (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),  # even length
    (["A"], ["A"]),  # single character
]

for s, expected in test_cases:
  reverse_string(s)
  assert s == expected, "Error"
