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

Backtracking is a problem-solving technique commonly used in LeetCode challenges,
especially for problems involving combinations, permutations, and decision-making trees.
It systematically explores all possible solutions to a problem by incrementally building
candidates and abandoning a candidate ("backtracking")
as soon as it determines that it cannot lead to a valid solution.

"""

def subsets_2(nums):
    return nums

if __name__ == "__main__":
    nums = [1,2,1]
    res = []
    nums.sort()

    def backtrack(i, subset):
        #i is the index we are considering
        if i == len(nums):
           res.append(subset[::])
           return

        #subset with nums[i]
        subset.append(nums[i])
        backtrack(i+1,subset)

        #subset without nums[i]
        subset.pop()

        #skip next index if it is same as current index
        while i + 1 < len(nums) and nums[i] == nums[i+1]:
            i += 1
        backtrack(i+1, subset)
        return res

    print(backtrack(0, []))

