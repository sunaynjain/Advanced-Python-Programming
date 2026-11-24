def knapsack_bottom_up(values, weights, W):
    n = len(values)
    dp = [[0 for i in range(W + 1)] for j in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


def knapsack_top_down(values, weights, W):
    n = len(values)
    dp = [[-1 for i in range(W + 1)] for j in range(n + 1)]

    def solve(n, W):
        if n == 0 or W == 0:
            return 0

        if dp[n][W] != -1:
            return dp[n][W]

        if weights[n - 1] <= W:
            dp[n][W] = max(
                values[n - 1] + solve(n - 1, W - weights[n - 1]),
                solve(n - 1, W)
            )
        else:
            dp[n][W] = solve(n - 1, W)

        return dp[n][W]

    return solve(n, W)


values = [60, 100, 120]
weights = [10, 20, 30]
W = 50

print("Bottom-Up Result:", knapsack_bottom_up(values, weights, W))
print("Top-Down Result:", knapsack_top_down(values, weights, W))
