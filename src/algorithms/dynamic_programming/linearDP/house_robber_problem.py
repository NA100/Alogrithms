"""
Problem
You’re given an array nums where nums[i] is the money in the i-th house on a street.
You can’t rob two adjacent houses. Maximize the total money.
"""

def house_robber_max_money(nums):
    dp = [0] * len(nums)
    for i in range(0, len(nums)):
        if i == 0:
            dp[i] = nums[i]
        else:
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

    print(dp)
    return dp[len(nums) - 1]

def main():
    nums = [10, 60, 50, 100, 210, 200]
    max_sum = house_robber_max_money(nums)
    print("maximum money that can be robbed: ", max_sum)

if __name__ == "__main__":
    main()