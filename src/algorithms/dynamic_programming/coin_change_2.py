"""
Unbounded Knapsack --
In the classic 0/1 Knapsack, you can take each item at most once.
In Unbounded Knapsack, you can take each item unlimited times —
 exactly like coins in the coin change problem.
Alright — Coin Change 2 is the count ways version of the coin change problem.
   Problem Statement
   Given:
   coins = list of distinct denominations.
   amount = target sum.
   Return: Number of combinations that make up that amount.
   Order of coins does not matter → {1,2} is the same as {2,1}.
"""

def coin_change(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for c in coins:                 # fix an order of coin TYPES
        for a in range(c, amount+1):
            dp[a] += dp[a - c]      # add ways that end with coin c
    return dp[amount]

def main():
    coins = [1, 2, 5]
    amount = 5
    print(coin_change(coins, amount))

if __name__ == "__main__":
    main()


"""
Example 1: coins = [1, 2], amount = 4
Start: dp = [1, 0, 0, 0, 0] (one way to make 0: take nothing)
Process coin 1
For a = 1..4: dp[a] += dp[a-1]
After coin 1: dp = [1, 1, 1, 1, 1]
(only “all 1s” so far)
Process coin 2
a = 2: dp[2] += dp[0] → 1 + 1 = 2
New ways for 2 from dp[0] + 2: {2}
a = 3: dp[3] += dp[1] → 1 + 1 = 2
New ways: ways to make 1 ({1}) + 2 → {1+2}
a = 4: dp[4] += dp[2] → 1 + 2 = 3
dp[2] currently has {1+1, 2}; add +2 → {1+1+2, 2+2}
Final dp = [1, 1, 2, 2, 3] → 3 ways to make 4:
1+1+1+1
1+1+2
2+2
"""