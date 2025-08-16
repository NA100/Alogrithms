"""
Problem
Given two strings word1 and word2, return the minimum number of operations required to convert word1 into word2.
Allowed operations:
Insert a character
Delete a character
Replace a character
"""

def min_edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base cases
    for i in range(m + 1):
        dp[i][0] = i  # deletions
    for j in range(n + 1):
        dp[0][j] = j  # insertions

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1,   # delete
                    dp[i][j - 1] + 1,   # insert
                    dp[i - 1][j - 1] + 1  # replace
                )
    return dp[m][n]


def main():
    print(min_edit_distance("horse", "ros"))   # Expected: 3
    print(min_edit_distance("intention", "execution"))  # Expected: 5


if __name__ == "__main__":
    main()
