"""
Given an integer array nums, return an array answer such that answer[i] is equal to
the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

TIP:  you actually don't need prefix array and suffix array
You can do passes one from left to right and right to left
In output array and update the value
"""

def product_except_self(nums):
    prefix_array = [0] * len(nums)
    suffix_array = [0] * len(nums)
    result_array = [0] * len(nums)

    for i in range(len(nums)):
        if i == 0:
            prefix_array[i] = nums[i]
        else:
            prefix_array[i] = prefix_array[i-1] * nums[i]

    for i in range(len(nums) - 1, -1, -1):
        if i == len(nums) - 1:
            suffix_array[i] = nums[i]
        else:
            suffix_array[i] = suffix_array[i+1] * nums[i]

    print(prefix_array)
    print(suffix_array)
    for i in range(len(nums)):
        if i == 0:
            result_array[i] = suffix_array[i+1]
        elif i == len(nums) - 1:
            result_array[i] = prefix_array[i-1]
        else:
            result_array[i] = prefix_array[i-1] * suffix_array[i+1]

    return result_array

if __name__ == "__main__":
    nums =  [1,2,3,4]
    print(product_except_self(nums))