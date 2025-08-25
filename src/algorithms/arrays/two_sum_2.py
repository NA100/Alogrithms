"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2]
where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2,
 added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution.
You may not use the same element twice.

Your solution must use only constant extra space.
"""


def two_sum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    i = 0
    j = len(numbers) - 1

    while i < j:
        if numbers[i] + numbers[j] == target:
            return [i+1,j+1]

        if numbers[i] + numbers[j] > target:
            j = j - 1
        else:
            i = i + 1

    return [-1, -1]


if __name__ == "__main__":
    nums = [2, 9 , 7, 1, 10]
    target = 9
    print(two_sum(nums, target))