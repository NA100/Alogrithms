"""
Top K Frequent Elements in an Array

Given an array arr[] and a positive integer k, the task is to find the
 k most frequently occurring elements from a given array.

Note: If more than one element has same frequency then prioritise the larger
element over the smaller one.

Examples:
Input: arr= [3, 1, 4, 4, 5, 2, 6, 1], k = 2
Output: [4, 1]
Explanation: Frequency of 4 is 2 and frequency of 1 is 2, these two have the
maximum frequency and 4 is larger than 1.

Input: arr = [7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9], k = 4
Output: [5, 11, 7, 10]
Explanation: Frequency of 5 is 3, frequency of 11 is 2, frequency of 7 is 2,
frequency of 10 is 1. These four have the maximum frequency and 5 is largest among rest.

Put in map
Sort map by values and return top 'k'

Sort the entire array
keep a min heap of size k

heap[0] is always the smallest element.
heappush inserts.
heappop removes the smallest.
"""
import heapq

def top_k_with_sorted_map(nums, k):
    map = {}
    res = []
    for i in nums:
        map.setdefault(i, 0)
        map[i] += 1

    sorted_map = dict(sorted(map.items(), key=lambda item:item[1], reverse=True))

    for key, value in sorted_map.items():
        if len(res) < k:
            res.append(key)
    return res


def top_k_with_heap(nums, k):
    heap = []
    dict = {}
    res = []
    for i in nums:
        dict.setdefault(i, 0)
        dict[i] += 1

    for key, value in dict.items():
        heapq.heappush(heap, (value,key))
        if len(heap) > k:
            heapq.heappop(heap)
        print(heap)
    for i in heap:
        res.append(i[1])
    return res


def top_k_bucket_sort(nums, k):
    #bucket = [[]] * (len(nums) + 1)
    bucket = [[] for i in range(len(nums) + 1)]
    map = {}
    res = []

    for i in nums:
        map.setdefault(i, 0)
        map[i] += 1
    print(map)

    for key, val in map.items():
        bucket[val].append(key)
    print(bucket)

    for l in range(len(bucket) - 1, -1, -1):
        if len(res) < k:
            for j in bucket[l]:
                res.append(j)
    return res


if __name__ == "__main__":
    nums = [1,1,1,2,2,2,3,3,3,3,3,3]
    k = 2
    print(top_k_with_heap(nums, k))