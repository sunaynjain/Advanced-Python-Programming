def unique_paths(m, n):
    dp = [[1] * n for i in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]


m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

print("Total unique paths:", unique_paths(m, n))
