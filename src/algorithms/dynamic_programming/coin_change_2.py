"""
Unbounded Knapsack --
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
    dp_table 

    for i in range(0 to len(coins)):

def main():
    coins = [1, 2, 5]
    amount = 5
    print(coin_change(coins, amount))

if __name__ == "__main__":
    main()