"""
You plan to travel on certain days of the year. Tickets are available in three types:
1-day pass (covers exactly 1 day)
7-day pass (covers 7 consecutive days)
30-day pass (covers 30 consecutive days)
Given the days you will travel and the cost of each ticket type, compute the minimum total cost to cover all travel days.
Input.
days: a strictly increasing list of integers representing travel days in the range 1..365.
costs: an array of three positive integers [cost1, cost7, cost30] for the 1-day, 7-day, and 30-day passes.
"""

def min_travel_cost(days, cost):
    n = len(days)
    dp = [0] * len(days)

    dp[0] = cost[0]
    adj = 1
    for i in range(1, n):
        if adj >= 7:
            dp[i] = min(dp[i-7] + cost[1], dp[i-1] + cost[0])
        if adj >= 15:
            dp[i] = min(dp[i-15] + cost[2], dp[i-1] + cost[0])
        if adj < 7:
            dp[i] = dp[i-1] + cost[0]
        if days[i-1] + 1 == days[i]:
            adj = adj + 1
        else:
            adj = 1
    return dp[n-1]

def main():
    days = [1, 4, 6, 7, 8, 20]
    cost = [2, 7, 15]
    print(min_travel_cost(days, cost))

if __name__ == "__main__":
    main()