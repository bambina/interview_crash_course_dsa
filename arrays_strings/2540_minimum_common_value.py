# Given two integer arrays nums1 and nums2, sorted in non-decreasing order,
# return the minimum integer common to both arrays.
# If there is no common integer amongst nums1 and nums2, return -1.
# Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

def minimum_common_value(nums1: list[int], nums2: list[int]) -> int:
  ptr_1 = ptr_2 = 0
  while ptr_1 < len(nums1) and ptr_2 < len(nums2):
    if nums1[ptr_1] == nums2[ptr_2]:
      return nums1[ptr_1]
    elif nums1[ptr_1] > nums2[ptr_2]:
      ptr_2 += 1
    else:
      ptr_1 += 1
  return -1


test_cases = [
    ([1, 2, 3], [2, 4], 2),
    ([1, 2, 3, 6], [4, 5, 6], 6),
    ([1, 2, 3], [4, 5, 6], -1),
    ([1], [1], 1),
    ([1], [2], -1),
]

for nums1, nums2, expected in test_cases:
  result = minimum_common_value(nums1, nums2)
  assert result == expected, f"Expected {expected}, got {result}"
