def min_path_sum_bottomup(grid):
    """
    Minimum path sum from grid[0][0] to grid[m-1][n-1],
    moving only right or down (bottom-up DP).
    """
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    dp[0][0] = grid[0][0]
    for j in range(1, n):
        dp[0][j] = grid[0][j] + dp[0][j - 1]
    for i in range(1, m):
        dp[i][0] = grid[i][0] + dp[i - 1][0]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

    return dp[m - 1][n - 1]


def min_path_sum_bottomup_with_path(grid):
    """
    Returns (min_sum, path) where path is a list of (i, j) from start to end.
    """
    if not grid or not grid[0]:
        return 0, []

    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    parent = [[None] * n for _ in range(m)]  # 'U' (came from up) or 'L' (came from left)

    dp[0][0] = grid[0][0]

    for j in range(1, n):
        dp[0][j] = grid[0][j] + dp[0][j - 1]
        parent[0][j] = 'L'

    for i in range(1, m):
        dp[i][0] = grid[i][0] + dp[i - 1][0]
        parent[i][0] = 'U'

    for i in range(1, m):
        for j in range(1, n):
            if dp[i - 1][j] <= dp[i][j - 1]:
                dp[i][j] = grid[i][j] + dp[i - 1][j]
                parent[i][j] = 'U'
            else:
                dp[i][j] = grid[i][j] + dp[i][j - 1]
                parent[i][j] = 'L'

    # reconstruct path from end to start
    i, j = m - 1, n - 1
    path = [(i, j)]
    while (i, j) != (0, 0):
        move = parent[i][j]
        if move == 'U':
            i -= 1
        else:  # 'L'
            j -= 1
        path.append((i, j))
    path.reverse()

    return dp[m - 1][n - 1], path


def min_path_sum_space_opt(grid):
    """
    Space-optimized O(n) bottom-up version (no path reconstruction).
    """
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    dp = [0] * n
    dp[0] = grid[0][0]

    for j in range(1, n):
        dp[j] = dp[j - 1] + grid[0][j]

    for i in range(1, m):
        dp[0] += grid[i][0]
        for j in range(1, n):
            dp[j] = grid[i][j] + min(dp[j], dp[j - 1])

    return dp[-1]


def main():
    grid = [
        [1, 3, 1, 4],
        [1, 5, 1, 2],
        [4, 2, 1, 7],
        [3, 1, 2, 3]
    ]
    total = min_path_sum_bottomup(grid)
    total2, path = min_path_sum_bottomup_with_path(grid)
    total3 = min_path_sum_space_opt(grid)

    print("Min path sum (bottom-up):", total)                # -> 12
    print("Min path sum (with path):", total2)               # -> 12
    print("Path:", path)                                     # e.g., [(0,0),(1,0),(2,0),(2,1),(2,2),(3,2),(3,3)]
    print("Min path sum (space-optimized):", total3)         # -> 12


if __name__ == "__main__":
    main()
