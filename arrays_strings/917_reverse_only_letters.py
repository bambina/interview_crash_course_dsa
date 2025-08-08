# Given a string s, reverse the string according to the following rules:
# - All the characters that are not English letters remain in the same position.
# - All the English letters(lowercase or uppercase) should be reversed.
# Return s after reversing it.

def reverse_only_letters(s: str) -> str:
  ans = list(s)
  l = 0
  r = len(s)-1
  while l < r:
    if ans[l].isalpha() and ans[r].isalpha():
      ans[l], ans[r] = ans[r], ans[l]
      l += 1
      r -= 1
    elif not ans[l].isalpha():
      l += 1
    else:
      r -= 1
  return "".join(ans)
  # left = 0
  # right = len(s)-1
  # ans = list(s)
  # while left < right:
  #   while left < right and not ans[left].isalpha():
  #     left += 1
  #   while left < right and not ans[right].isalpha():
  #     right -= 1
  #   ans[left], ans[right] = ans[right], ans[left]
  #   left += 1
  #   right -= 1
  # return "".join(ans)


test_cases = [
    ("ab-cd", "dc-ba"),
    ("a-bC-dEf-ghIj", "j-Ih-gfE-dCba"),
    ("7_28]", "7_28]"),
    ("?6C40E", "?6E40C"),
]

for s, expected in test_cases:
  result = reverse_only_letters(s)
  assert result == expected, f"Expected {expected}, got {result}"
