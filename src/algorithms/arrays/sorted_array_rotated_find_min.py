"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the
 array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

"""

def find_min(arr):
    l = 0
    h = len(arr) - 1
    m = -1

    while l <= h:
        m = (l + h) // 2
        if arr[l] < arr[h]:
            m = l
            break
        if arr[l] > arr[m]:
            h = m - 1
        else:
            l = m + 1
    return arr[m]

if __name__ == "__main__":
    arr = [11,1,2,3,4,5,6,7,8]
    print(find_min(arr))