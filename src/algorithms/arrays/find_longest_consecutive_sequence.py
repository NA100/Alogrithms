"""
Given an unsorted array of integers nums, return the length of the longest
consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3

"""

def longest_sequence(nums):
    num_set = set(nums)
    best = 0


    for s in num_set: #iterate thru all elements in set
        if s-1 not in num_set:  # only start counting at beginning of sequence
            y = s
            while y in num_set:
                y += 1
            best = max(best, y - s)
    return best



if __name__ == "__main__":
    nums = [100,4,200,1,3,2]
    print(longest_sequence(nums))