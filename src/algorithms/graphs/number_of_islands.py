"""
Number of Islands — Problem Statement
Description
Given an m x n 2D grid map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically (4-directional). You may assume all four edges of the grid are surrounded by water.
Input Format (one common console format)

First line: two integers m n — number of rows and columns.
Next m lines: each line has n characters, each either 0 or 1 (optionally separated by spaces).
Alternate (LeetCode style): grid is provided as List[List[str]], where each entry is '0' or '1'.
Output Format
One integer: the number of islands.
Constraints
1 ≤ m, n ≤ 300
grid[i][j] ∈ {'0','1'}

Example 1
Input
4 5
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1
Output
3
Explanation
There are three separate land clusters: a 2×2 block at top-left, a single cell at (2,2), and a 2-cell cluster at bottom-right.
"""