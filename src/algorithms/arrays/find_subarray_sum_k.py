"""
Given an array of integers nums and an integer k, return the total number of
subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

Kadane's algorithm:
Brute-force is O(n square) - every single subarray
Keep track of prefix-sum and count
Intuition - can you chop off something and make sum = k
Iterate O(n) and find everything exhaustively

"""

def sub_array_sum(nums, k):
    res = 0
    cur_sum = 0
    prefix_sum = {0: 1}

    for i in nums:
        cur_sum = cur_sum + i
        diff = cur_sum - k

        matches = prefix_sum.get(diff, 0)
        res += matches

        prefix_sum[cur_sum] = prefix_sum.get(cur_sum, 0) + 1

    return res

if __name__ == "__main__":
    nums = [1,1,1]
    k = 2
    print(sub_array_sum(nums, k))