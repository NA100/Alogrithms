"""
Got it — Delete Operation for Two Strings is a simplified version of the Edit Distance problem.
The only allowed operation is deletion, so we don’t need to handle insert or replace separately.
Problem
Given:
Two strings word1 and word2
Return: The minimum number of deletions needed to make the two strings equal.

If we know the Longest Common Subsequence (LCS) between the two strings, then:
Characters not in the LCS must be deleted.
If:
m = len(word1)
n = len(word2)
lcs = length of LCS(word1, word2)

"""

def min_deletions_to_equal(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # LCS computation
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs_length = dp[m][n]
    return (m - lcs_length) + (n - lcs_length)


def main():
    print(min_deletions_to_equal("sea", "eat"))  # Expected: 2
    print(min_deletions_to_equal("leetcode", "etco"))  # Expected: 4


if __name__ == "__main__":
    main()
