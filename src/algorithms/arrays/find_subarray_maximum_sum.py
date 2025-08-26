"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

What is Kadane’s Algorithm?
Kadane’s Algorithm is a dynamic programming algorithm used to
solve the maximum subarray problem.
keeping track of the current subarray sum, updating it as it goes along.
The algorithm returns the maximum subarray sum found.

Advantages
- Kadane’s Algorithm is efficient and requires only a single scan
through the array.
- The algorithm is simple to understand and implement.
It works well for arrays with both positive and negative numbers.

Disadvantages
- Kadane’s Algorithm only works for arrays with at least one
positive number. If all numbers in the array are negative,
the algorithm will return 0 as the maximum subarray sum.
- The algorithm may not work for arrays with very large or
very small values, as it can suffer from overflow or underflow issues.
"""

def find_max_subarray(nums):
    max_sum = 0
    cur_sum = 0
    for n in nums:
        if cur_sum < 0:
            cur_sum = 0
        cur_sum = cur_sum + n
        max_sum = max(cur_sum, max_sum)
    return max_sum

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(find_max_subarray(nums))