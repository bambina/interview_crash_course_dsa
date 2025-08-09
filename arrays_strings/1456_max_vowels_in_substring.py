# Given a string s and an integer k,
# return the maximum number of vowel letters in any substring of s with length k.
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

def maxVowels(s: str, k: int) -> int:
  if len(s) < k:
    return 0

  left = curr = 0
  vowels = set('aeiou')
  for right in range(k):
    if s[right] in vowels:
      curr += 1

  ans = curr
  for right in range(k, len(s)):
    if s[right] in vowels:
      curr += 1
    if s[left] in vowels:
      curr -= 1
    ans = max(ans, curr)
    left += 1

  return ans


test_cases = [
    ("abciiidef", 3, 3),
    ("aeiou", 2, 2),
]

for target, nums, expected in test_cases:
  res = maxVowels(target, nums)
  assert res == expected, f"Expected {expected}, got {res}"
