
def max_sum_non_adjacent(nums):
    dp = [0] * len(nums)
    for i in range(0, len(nums)):
        if i == 0:
            dp[i] = nums[i]
        else:
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

    print(dp)
    return dp[len(nums) - 1]

def main():
    nums = [5, -10, 4, 3, 2]
    max_sum = max_sum_non_adjacent(nums)
    print("maximum sum non-adjacent: ", max_sum)

if __name__ == "__main__":
    main()