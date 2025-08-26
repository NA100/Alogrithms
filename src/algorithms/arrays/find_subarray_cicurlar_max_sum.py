"""
Given a circular integer array nums of length n,
return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array.
Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of
nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once.
Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not
exist i <= k1, k2 <= j with k1 % n == k2 % n.

Example 1:

Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.
Example 2:

Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
Example 3:

Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.

"""

def find_max_subarray(nums):
    glo_min = nums[0]
    glo_max = nums[0]
    cur_min = 0
    cur_max = 0
    total =  0

    for n in nums:
        total += n

        cur_max = max(cur_max + n, n)
        glo_max = max(cur_max, glo_max)

        cur_min = min(cur_min + n, n)
        glo_min = min(cur_min, glo_min)

    return max(glo_max, total - glo_min) if glo_max > 0 else glo_max

if __name__ == "__main__":
    nums = [5,-3,5]
    print(find_max_subarray(nums))