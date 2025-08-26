"""
You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints
of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container,
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Brute force way
i = 0, j = 1 test all combinations and return max - O(n square)

i = 0, j = n - 1 optimized solution T = O(n) and S = O(1)
"""

def container_with_most_water(height):
    n = len(height)
    i = 0
    j = n - 1
    max_water = 0
    while i < j:
        water =  min(height[i], height[j]) * (j - i)
        max_water = max(water, max_water)
        if height[i] < height[j]:
            i = i + 1
        else:
            j = j - 1
    return max_water


if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    print(container_with_most_water(height))