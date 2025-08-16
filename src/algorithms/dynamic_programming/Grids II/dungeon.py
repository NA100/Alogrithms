"""
Problem
You’re a knight starting at the top-left of a dungeon grid, trying to rescue the princess at the bottom-right.
Each cell has:
Negative value → damage (lose HP)
Positive value → health potion (gain HP)
You can only move right or down.
Goal: Find the minimum initial health you must start with so that you never drop to 0 HP or below at any point.
Example
[[-2, -3,  3],
 [-5, -10, 1],
 [10,  30, -5]]
Output:
7
Why:
Path: Right → Right → Down → Down
Starting with 7 HP ensures that even after the worst hits, your HP stays ≥ 1.
"""