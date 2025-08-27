"""
Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Brute-force
* merge both arrays O(m+n)

Optiomal solution
* Use binary search log(m+n)


Here's the intuition that helped me understand this. In this problem, we are searching for the
"correct partition" in an array, such that,

1. Number of elements in the merged array is (m+n) // 2
2. All the elements in the left partition of both the arrays are lesser than or equal to all the
elements in the right partition of both the arrays
3. If ALeft > BRight --- move the partition to right in nums2 (i.e. move to left in nums1)
4. If BLeft > ARight --- move the partition to left in nums2 (i.e. move to right in nums1)


"""

def find_median(nums1, nums2):
    total = (len(nums1) + len(nums2))
    half = total // 2

    if nums1 > nums2:
        nums1, nums2 = nums2, nums1

    l = 0
    r = len(nums1) - 1

    while True:
        i = (l + r) // 2  #partition of nums1
        j = half - i - 2  #partition of nums2

        a_left = nums1[i] if i >= 0 else float('-inf')
        a_right = nums1[i+1] if (i + 1) < len(nums1) else float('inf')
        b_left = nums2[j] if j >= 0 else float('-inf')
        b_right = nums2[j+1] if (j + 1) < len(nums1) else float('inf')

        if (a_left <= b_right) and (b_left <= a_right):
            if total % 2:
                return min(a_right, b_right)
            else:
                return (max(a_left, b_left) + min(b_right, a_right)) / 2
        elif a_left > b_right:
            r = i - 1
        else:
            l = i + 1

    return 0

if __name__ == "__main__":
    nums1 = [1,3]
    nums2 = [2]
    median = find_median(nums1, nums2)
    print(f"Median is {median}")