"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Min-Heap (O(n log k))

"""
import heapq

def find_kth_largest(nums, k):
    heap = []

    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)

    return heapq.heappop(heap) #heap[0]


if __name__ == "__main__":
    nums = [3,2,1,5,6,4]
    k = 2
    print(find_kth_largest(nums, k))