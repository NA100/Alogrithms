# Module 1 code here
"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

class Solution(object):
    def climbStairs(self, n):
        climb = [0] * (n + 1)  # create an array of size n+1
        climb[0] = 1           # 1 way to stand at step 0
        climb[1] = 1           # 1 way to reach step 1
        for i in range(2, n + 1):
            climb[i] = climb[i-1] + climb[i-2]  # DP relation
        return climb[n]


    def climbStairs_SpaceEfficient(self, n):
            first = 1           # 1 way to stand at step 0
            second = 2           # 1 way to reach step 1
            current = 1
            for i in range(3, n + 1):
                current = first + second
                first = second
                second = current
            return current


def main():
    # Example usage
    n = int(input("Enter number of steps: "))
    solver = Solution()
    result = solver.climbStairs_SpaceEfficient(n)
    print(f"Number of distinct ways to climb {n} steps: {result}")

if __name__ == "__main__":
    main()