class Solution(object):
    def uniquePaths(m, n):
        dp = [[1] * n for _ in range(m)]             #m->rows
                                                    #n->columns

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]



