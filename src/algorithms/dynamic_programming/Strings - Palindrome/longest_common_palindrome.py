"""
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
"""

def longest_palindrome_dp(s: str) -> str:
    n = len(s)
    if n < 2:
        return s
    dp = [[False]*n for _ in range(n)]
    start, max_len = 0, 1
    for i in range(n):
        dp[i][i] = True
    for L in range(2, n+1):              # substring length
        for i in range(n - L + 1):
            j = i + L - 1
            if s[i] == s[j] and (L == 2 or dp[i+1][j-1]):
                dp[i][j] = True
                if L > max_len:
                    start, max_len = i, L
    return s[start:start+max_len]

if __name__ == "__main__":
    print(longest_palindrome_dp("afeghsdfasooobabab"))