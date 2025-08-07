# Given a string s, reverse the order of characters in each word within a sentence
# while still preserving whitespace and initial word order.

def reverse(l: list[str], start: int, end: int):
  while start < end:
    l[start], l[end] = l[end], l[start]
    start += 1
    end -= 1


def reverse_words(s: str) -> str:
  ans = list(s)
  n = len(s)
  left = right = 0
  while left < n:
    # Skip spaces to find the beginning of the word
    while left < n and ans[left] == " ":
      left += 1
    right = left
    # Move right to the end of the word (until the next space or end of string)
    while right < n and ans[right] != " ":
      right += 1

    reverse(ans, left, right-1)
    left = right
  return "".join(ans)

  # words = s.split()
  # for i in range(len(words)):
  #   words[i] = words[i][::-1]
  # return " ".join(words)


test_cases = [
    ("hello world", "olleh dlrow"),
    ("a", "a"),
    ("ab", "ba"),
    ("", ""),
    ("Mr Ding", "rM gniD"),
]

for s, expected in test_cases:
  result = reverse_words(s)
  assert result == expected, f"Expected {expected}, got {result}"
