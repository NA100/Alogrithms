from functools import lru_cache
from math import inf

def min_path_sum_topdown(grid):
    """
    Minimum path sum from grid[0][0] to grid[m-1][n-1],
    moving only right or down (top-down + memoization).
    """
    if not grid or not grid[0]:
        return 0
    m, n = len(grid), len(grid[0])

    @lru_cache(None)
    def dp(i, j):
        if i == m or j == n:
            return inf
        if i == m - 1 and j == n - 1:
            return grid[i][j]
        return grid[i][j] + min(dp(i + 1, j), dp(i, j + 1))

    return dp(0, 0)

def min_path_sum_topdown_with_path(grid):
    """
    Returns (min_sum, path) where path is a list of (i, j) from start to end.
    """
    if not grid or not grid[0]:
        return 0, []
    m, n = len(grid), len(grid[0])

    @lru_cache(None)
    def dp(i, j):
        if i == m or j == n:
            return inf
        if i == m - 1 and j == n - 1:
            return grid[i][j]
        return grid[i][j] + min(dp(i + 1, j), dp(i, j + 1))

    total = dp(0, 0)

    # Reconstruct path by greedily following the cheaper next move using dp()
    path, i, j = [(0, 0)], 0, 0
    while i != m - 1 or j != n - 1:
        down = dp(i + 1, j)
        right = dp(i, j + 1)
        if down <= right:
            i += 1
        else:
            j += 1
        path.append((i, j))

    return total, path

def main():
    grid = [
        [1, 3, 1, 4],
        [1, 5, 1, 2],
        [4, 2, 1, 7],
        [3, 1, 2, 3]
    ]
    total = min_path_sum_topdown(grid)
    total2, path = min_path_sum_topdown_with_path(grid)
    print("Min path sum:", total)                 # -> 12
    print("Min path sum (with path):", total2)    # -> 12
    print("Path:", path)                          # e.g., [(0,0), (1,0), (2,1), (2,2), (3,2), (3,3)]

if __name__ == "__main__":
    main()
