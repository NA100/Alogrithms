"""
You are given an array nums of integers, which may contain duplicates. Return all possible subsets.

The solution must not contain duplicate subsets. You may return the solution in any order.

Example 1:

Input: nums = [1,2,1]

Output: [[],[1],[1,2],[1,1],[1,2,1],[2]]
Example 2:

Input: nums = [7,7]

Output: [[],[7], [7,7]]
Constraints:

1 <= nums.length <= 11
-20 <= nums[i] <= 20

- Sort to group duplicates.
- Walk the array in “runs”: pick a value val and count how many times it repeats (cnt).
- For every current subset base in res, append val k times for k = 1..cnt.
(The k=0 case is “do nothing,” already covered by keeping base.)
This guarantees uniqueness: for each distinct value you choose exactly
how many copies (0..cnt) to include—no other way can produce a different multiset.
"""

def subsets_2(nums):
    return nums

if __name__ == "__main__":
    nums = [1, 2, 1]
    nums.sort()
    res = [[]]
    i = 0

    while i < len(nums):
        count = 1
        while (i+1 < len(nums) and nums[i] == nums[i+1]):
            i += 1
            count += 1
        for j in range(0, len(res)):
            print(f"adding {nums[i]} to {res[j]} at index {i}")
            for k in range(1, count+1):
                new_val = res[j] + [nums[i]] * k
                print(f"adding {new_val} to {res}")
                res.append(new_val)
        i += 1
    print(res)
