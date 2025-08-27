"""
Given an array nums of n integers, return an array of all the unique
quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

"""

def k_sum(nums, target, k):
    nums.sort()
    print(nums)
    res = []
    quad = []

    def helper(target, start, k):
        if k > 2:
            for i in range(start, len(nums) - k + 1):
                if i > start and nums[i] == nums[i-1]:
                    continue
                quad.append(nums[i])
                helper(target - nums[i], i + 1, k - 1)
                quad.pop()
            return

        print(quad)
        l = start
        r = len(nums) - 1
        print(target)
        while r > l:
            if nums[r] + nums[l] == target:
                print(f"adding to result {l} and {r}")
                res.append(quad + [nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
            elif nums[r] + nums[l] > target:
                r -= 1
            else:
                l += 1

    helper(target, 0, 4)
    return res

if __name__ == "__main__":
    nums = [1,0,-1,0,-2,2]
    target = 0
    k = 4
    print(k_sum(nums, target, k))