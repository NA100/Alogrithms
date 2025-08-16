"""
Problem
Given an m x n grid of 0s (water) and 1s (land), return the area (cell count) of the largest island.
Cells connect up, down, left, right (4-directional). If no land exists, return 0.
Input format (console style)
First line: m n
Next m lines: n integers (0/1) optionally space-separated.
Output
Single integer: maximum island area.
Example
Input
4 5
1 1 0 0 0
1 1 0 1 1
0 0 1 0 0
0 0 0 1 1
Output
4
Why: The biggest island has 4 cells (the bottom-right cluster).
"""