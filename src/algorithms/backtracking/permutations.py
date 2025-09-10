"""
Given an array nums of unique integers, return all the possible permutations.
You may return the answer in any order.

Example 1:

Input: nums = [1,2,3]

Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [7]

Output: [[7]]
Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10

Time complexity - O(N factorial * n)
"""
def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    def per(prefix, rem_nums):
        if len(rem_nums) == 1:
            val = prefix + rem_nums
            res.append(val)
        for i in range(0,len(rem_nums)):
            per(prefix+[rem_nums[i]], rem_nums[0:i]+rem_nums[i+1:len(nums)])

    per([], nums)
    print(res)
    return res

if __name__ == "__main__":
    permute([1,2,3])
