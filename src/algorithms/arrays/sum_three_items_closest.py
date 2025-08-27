"""
Given an integer array nums of length n and an integer target,
find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

"""
def three_sum_closest(nums, target):
    nums.sort()
    closest_diff = float('inf')

    for i in range(0, len(nums) - 2):
        l = i + 1
        r = len(nums) - 1
        new_target = target - nums[i]
        while l < r:
            sum = nums[l] + nums[r]
            if sum == new_target:
                return new_target + sum
            elif sum < new_target:
                l += 1
                closest_diff = min(closest_diff, abs(sum - new_target))
            else:
                r -= 1
                closest_diff = min(closest_diff, abs(sum - new_target))

    return target - closest_diff


if __name__ == "__main__":
    nums = [-1,2,1,-4]
    target = -5
    print(three_sum_closest(nums, target))