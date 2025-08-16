"""
Alright — Burst Balloons is a famous interval DP problem that’s conceptually very similar to Matrix Chain Multiplication (MCM) but with a twist: instead of multiplying matrices, you’re bursting balloons for coins.
Problem
You are given n balloons, each with a number on it.
When you burst balloon i, you gain:
nums[left]×nums[i]×nums[right]
where left and right are the balloons adjacent to i after the previous bursts (if no balloon, treat as 1).
Goal: Burst all balloons to maximize coins.
Example
nums = [3, 1, 5, 8]
We pad with 1 at both ends: [1, 3, 1, 5, 8, 1].
One optimal way:
Burst 3 → gain 1×3×1 = 3
Burst 1 → gain 1×1×5 = 5
Burst 5 → gain 1×5×8 = 40
Burst 8 → gain 1×8×1 = 8
Total = 56
But the optimal sequence actually yields 167 coins.
"""