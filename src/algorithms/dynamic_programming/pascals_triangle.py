def pascal_triangle(n):
    # Initialize dp table with all 1's in each row
    dp = [[1] * (i + 1) for i in range(n + 1)]

    # Fill in middle values using Pascal's rule
    for i in range(2, n + 1):         # start from row 2
        for j in range(1, i):         # skip first & last element in each row
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    return dp


def main():
    n = 5  # number of rows - 1 (so this gives 6 rows: row 0 to row 5)
    triangle = pascal_triangle(n)

    # Print the triangle nicely
    for row in triangle:
        print(row)


if __name__ == "__main__":
    main()
