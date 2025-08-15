"""
Problem
Given:
An array of positive integers nums.
Return: True if the array can be partitioned into two subsets
with equal sum, otherwise False.
"""

def can_partition(nums):
    total = sum(nums)
    # If sum is odd, cannot split equally
    if total % 2 != 0:
        return False

    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True  # sum 0 is always possible (take no elements)

    for num in nums:
        # Go backwards to avoid reusing the same number
        for s in range(target, num - 1, -1):
            dp[s] = dp[s] or dp[s - num]

    return dp[target]


def main():
    nums = [1, 5, 11, 5]
    print(f"Can partition? {can_partition(nums)}")  # Expected: True

    nums = [1, 2, 3, 5]
    print(f"Can partition? {can_partition(nums)}")  # Expected: False


if __name__ == "__main__":
    main()
