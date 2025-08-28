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
        print(f"executing for : {arr[l]} {arr[m]} {arr[h]}")
        if arr[l] < arr[h]:
            m = l
            print(f"match : {arr[l]} {arr[h]}")
            break
        if arr[l] > arr[m]:
            h = m
            print(f"check left : {arr[l]} {arr[h]}")
        else:
            l = m + 1
            print(f"check right : {arr[l]} {arr[h]}")
    return arr[m]

if __name__ == "__main__":
    arr = [11,12,14, -1000, 0,1,2,3,4,5,6,7,8]
    print(find_min(arr))