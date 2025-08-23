"""
You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints
of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container,
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


4 2 2 4

4 3 4 5 4 5

prev - higher
cur - lower
next - higher (if > prev) stop
"""
