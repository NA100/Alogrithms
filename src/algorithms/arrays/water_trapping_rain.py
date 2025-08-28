"""
Given n non-negative integers representing an elevation map where the width of each
bar is 1, compute how much water it can trap after raining.

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array
 [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
"""

def rain_water(height):
    n = len(height)
    max_from_left = [0] * n
    max_from_right = [0] * n
    for i in range(0, n):
        if i > 0:
            max_from_left[i] = (max(max_from_left[i-1], height[i]))
        else:
            max_from_left[i] = (height[i])

    for i in range(n - 1, -1, -1):
        if i < n - 1:
            max_from_right[i] = max(max_from_right[i+1], height[i])
        else:
            max_from_right[i] = height[i]

    print(f"current height            {height}")
    print(f"max value from left side  {max_from_left}" )
    print(f"max value from right side {max_from_right}")
    water = 0
    for i in range(0, n):
        if i > 0 and i < (n - 1):
            c = min(max_from_left[i-1], max_from_right[i+1]) - height[i]
            if c > 0:
                print(f"water at position {i} for {height[i]}   : {c}")
                water += c
            else:
                print(f"No water at position {i} for {height[i]}: 0")

    return water

if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(rain_water(height))