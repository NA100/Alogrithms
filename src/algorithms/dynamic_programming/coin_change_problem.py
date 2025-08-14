"""
Problem: Coin Change (Minimum Coins)
You’re given a list of coin denominations and a target amount.
Return the minimum number of coins needed to make the target amount.
If it’s not possible, return -1.
"""

def coin_change_min_coins(coins, amount):
    """
    Return the minimum number of coins needed to make `amount`.
    If it's impossible, return -1.

    coins: list of positive integers (denominations)
    amount: non-negative integer
    """
    if amount == 0:
        return 0
    if not coins:
        return -1

    INF = amount + 1  # larger than any possible number of coins
    dp = [INF] * (amount + 1)
    dp[0] = 0  # base: 0 coins to make 0

    # Build answers for all amounts 1..amount
    for x in range(1, amount + 1):
        for c in coins:
            if c <= x:
                dp[x] = min(dp[x], dp[x - c] + 1)

    return dp[amount] if dp[amount] != INF else -1


def main():
    coins = [1, 2, 5]
    amount = 11
    ans = coin_change_min_coins(coins, amount)
    print(f"Minimum coins to make {amount} from {coins}: {ans}")


if __name__ == "__main__":
    main()
