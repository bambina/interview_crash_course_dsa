# Example 1:
# Given an array of strings strs, group the anagrams together.
# For example, given strs = ["eat", "tea","tan","ate","nat","bat"],
# return [["bat"],["nat","tan"],["ate","eat","tea"]].

from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
  hm = defaultdict(list)
  for str in strs:
    key = "".join(sorted(str))
    hm[key].append(str)
  return list(hm.values())


test_cases = [
    # Test case 1: Basic example from problem description
    (["eat", "tea", "tan", "ate", "nat", "bat"],
     [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]),

    # Test case 2: Empty array
    ([], []),

    # Test case 3: Single character strings and duplicates
    (["a", "aa", "aaa"], [["a"], ["aa"], ["aaa"]]),
]

for strs, expected in test_cases:
  result = sorted([sorted(group) for group in group_anagrams(strs)])
  assert result == expected, f"Error: input={strs}, expected={expected}, got={result}"
