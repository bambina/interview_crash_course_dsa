# Given a 0-indexed string word and a character ch,
# reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive).
# If the character ch does not exist in word, do nothing.

def reverse_prefix_of_word(word: str, ch: str) -> str:
  # idx = word.find(ch)
  # if idx == -1:
  #   return word
  # return word[:idx+1][::-1] + word[idx+1:]
  right = 0
  ans = list(word)
  for i in range(len(word)):
    if ans[i] == ch:
      right = i
      break

  left = 0
  while left < right:
    ans[left], ans[right] = ans[right], ans[left]
    left += 1
    right -= 1
  return "".join(ans)


test_cases = [
    ("abcdefd", "d", "dcbaefd"),
    ("xyxzxe", "z", "zxyxxe"),
    ("abcd", "z", "abcd"),
]

for word, ch, expected in test_cases:
  res = reverse_prefix_of_word(word, ch)
  assert res == expected, f"Expected {expected}, got {res}"
