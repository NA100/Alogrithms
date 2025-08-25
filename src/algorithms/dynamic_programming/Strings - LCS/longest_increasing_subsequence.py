"""
Problem
Given an integer array nums, return the length of the longest strictly increasing
subsequence.
A subsequence is a sequence that can be derived from another array by deleting some
elements (without changing the order of the remaining).

Example
    Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]
    Output: 4

Why: LIS is [2, 3, 7, 101]. Length = 4.
"""

class Solution(object):
    def longestIncreasingSubsequence(self, nums):
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        best = 1
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            best = max(best, dp[i])
        return best

def main():
    sol = Solution()
    nums = [10, 1, 2, 5, 3, 7, 101, 18]
    result = sol.longestIncreasingSubsequence(nums)
    print(f"LIS for '{nums}' : {result}")

if __name__ == "__main__":
    main()