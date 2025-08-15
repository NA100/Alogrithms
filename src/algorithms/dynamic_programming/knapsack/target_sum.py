"""
Problem
Given:
nums: list of non-negative integers
target: integer target value
You can put a + or − sign in front of each number.
Return: The number of ways to assign signs so that the sum equals target.
"""

def find_target_sum_ways(nums, target):
    total = sum(nums)
    # Check feasibility
    if (target + total) % 2 != 0 or abs(target) > total:
        return 0

    subset_sum = (target + total) // 2

    dp = [0] * (subset_sum + 1)
    dp[0] = 1  # One way to make sum 0 (choose nothing)

    for num in nums:
        for s in range(subset_sum, num - 1, -1):
            dp[s] += dp[s - num]

    return dp[subset_sum]

def main():
    nums = [1, 1, 1, 1, 1]
    target = 3
    result = find_target_sum_ways(nums, target)
    print(f"Ways to reach target {target}: {result}")  # Expected: 5

if __name__ == "__main__":
    main()
