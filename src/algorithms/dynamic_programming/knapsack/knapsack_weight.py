"""
Problem Statement
You are given:
n items, each with a weight and a value.
A knapsack with capacity W.
Goal: Pick a subset of items (each at most once) so that:
Total weight ≤ W
Total value is maximized.
"""

def knapsack_01(weights, values, W):
    """
    Solve the 0/1 Knapsack problem using 1D DP array.
    weights: list of item weights
    values:  list of item values
    W:       knapsack capacity
    Returns the maximum value achievable.
    """
    n = len(weights)

    # dp[w] = max value achievable with current capacity w
    # Initialize with 0 (value = 0 if no items or capacity is 0)
    dp = [0] * (W + 1)

    # Process each item one by one
    for i in range(n):
        w_i = weights[i]  # weight of current item
        v_i = values[i]   # value of current item

        # We go backwards (from high capacity to low capacity)
        # This ensures each item is only considered once (0/1 knapsack rule)
        for w in range(W, w_i - 1, -1):
            # Option 1: skip this item → value stays dp[w]
            # Option 2: take this item → value = v_i + best for (w - w_i)
            dp[w] = max(dp[w], v_i + dp[w - w_i])

            # At this point, dp[w] holds the best value considering items 0..i for capacity w

    # Answer is the best value for full capacity W
    return dp[W]


def main():
    # Example input
    weights = [2, 3, 4, 5]
    values  = [3, 4, 5, 8]
    W = 5

    result = knapsack_01(weights, values, W)
    print(f"Maximum value for capacity {W}: {result}")


if __name__ == "__main__":
    main()

