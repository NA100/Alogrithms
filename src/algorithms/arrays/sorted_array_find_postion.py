"""
Given an array of integers nums sorted in non-decreasing order,
 find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
"""

# O(logn)
def find_position_optimized(nums, target, leftBias):

    def binary_search_optimized(i, j, target, leftBias):
        k = -1
        while i <= j:
            mid = (j + i) // 2
            if nums[mid] < target:
                i = mid + 1
            elif nums[mid] > target:
                j = mid - 1
            else:
                k = mid
                if leftBias:
                    j = mid -1
                else:
                    i = mid + 1
        return k

    return binary_search_optimized(0, len(nums) -1, target, leftBias)


# O(n)
def find_position_not_optimized(nums, target):

    def binary_search(i, j, target):
        while i <= j:
            mid = i + ((j - i) // 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return -1

    closet_index = binary_search(0, len(nums) - 1, target)
    if closet_index == -1:
        return [-1, -1]

    i = closet_index
    j = closet_index
    while i < len(nums) and i > 0 and j < len(nums):
        if nums[j+1] == nums[j]:
            j = j + 1
        elif nums[i - 1] == nums[i]:
            i = i - 1
        else:
            return[i,j]

    return [i,j]


if __name__ == "__main__":
    nums = [5,7,7,8,8,10]
    target = 8
    print(find_position_not_optimized(nums, target))
    print(find_position_optimized(nums, target, True))
    print(find_position_optimized(nums, target, False))