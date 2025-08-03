# Example 4:
# Given an n x n matrix grid,
# return the number of pairs(R, C) where R is a row and C is a column,
# and R and C are equal if we consider them as 1D arrays.
from collections import defaultdict


def equal_pairs(grid: list[list[int]]) -> int:
  hm_row = defaultdict(int)
  hm_col = defaultdict(int)
  n = len(grid)

  for row in grid:
    hm_row[tuple(row)] += 1

  for c in range(n):
    col = []
    for r in range(n):
      col.append(grid[r][c])
    hm_col[tuple(col)] += 1

  ans = 0
  for key in hm_row:
    ans += hm_row[key] * hm_col[key]
  return ans


test_cases = [
    # Basic case: one matching pair
    ([[3, 2, 1], [1, 7, 6], [2, 7, 7]], 1),

    # Multiple pairs case
    ([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]], 3),

    # All rows and columns identical
    ([[1, 1], [1, 1]], 4),  # 2 rows × 2 columns = 4 pairs
]

for grid, expected in test_cases:
  result = equal_pairs(grid)
  assert result == expected, f"Error: grid={grid}, expected={expected}, got={result}"
