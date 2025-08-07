# Example 2: You are given a binary string s (a string containing only "0" and "1").
# You may choose up to one "0" and flip it to a "1".
# What is the length of the longest substring achievable that contains only "1"?

def find_length(s: str) -> int:
  left = curr = res = 0
  for right in range(len(s)):
    if s[right] == "0":
      curr += 1
      while curr > 1:
        if s[left] == "0":
          curr -= 1
        left += 1
    res = max(res, right-left+1)
  return res


test_cases = [
    ("1101100111", 5),    # flip middle "0" in "11011" -> "11111" (length 5)
    # flip first "0" -> "11011", longest "1" substring is "111" after flipping second "0" -> length 3
    ("10011", 3),
]

for s, expected in test_cases:
  result = find_length(s)
  assert result == expected, f"Error: s='{s}', got {result}, expected {expected}"
