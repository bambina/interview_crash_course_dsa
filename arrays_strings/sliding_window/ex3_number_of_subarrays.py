# Example 3: Given an array of positive integers nums and an integer k,
# return the number of subarrays where the product of all the elements in the subarray is strictly less than k.

def num_subarray_product_less_than_k(nums: list[int], k: int) -> int:
  if k <= 1:
    return 0

  left = ans = 0
  curr = 1

  for right in range(len(nums)):
    curr *= nums[right]
    while curr >= k:
      curr //= nums[left]
      left += 1

    ans += right - left + 1
  return ans


test_cases = [
    ([10, 5, 2, 6], 100, 8),
    ([1, 2, 3], 0, 0),
    ([1, 1, 1], 2, 6),
    ([100], 50, 0),
    ([2, 3, 4], 1, 0),
]

for nums, k, expected in test_cases:
  result = num_subarray_product_less_than_k(nums, k)
  assert result == expected, f"Error: nums={nums}, k={k}, expected={expected}, got={result}"
