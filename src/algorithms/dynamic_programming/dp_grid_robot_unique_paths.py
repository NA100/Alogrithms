"""
Statement:
A robot is located at the top-left corner of an m x n grid.
The robot can only move either down or right at any point in time.
How many unique paths are there to reach the bottom-right corner?

Constraints:
Only right or down moves allowed

No obstacles:
Grid size: m rows and n columns

"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1]*n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]

def main():
    sol = Solution()
    m, n = 3, 7
    result = sol.uniquePaths(m, n)
    print(f"Unique paths in a {m}x{n} grid: {result}")

if __name__ == "__main__":
    main()