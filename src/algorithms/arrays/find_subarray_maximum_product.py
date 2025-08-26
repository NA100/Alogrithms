"""
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

"""

def find_max_product_subarray(nums):
    cur_min = 1
    cur_max = 1
    res = max(nums)

    for n in nums:
        if n == 0:
            cur_max = 1
            cur_min = 1
            continue

        tmp = n * cur_max
        cur_max = max(cur_min * n, cur_max * n, n)
        cur_min = min(cur_min * n, tmp, n)
        res = max(cur_max, res)

    return res

if __name__ == "__main__":
    nums = [2,3,-2,4]
    print(find_max_product_subarray(nums))