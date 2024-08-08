class Solution(object):
    def numSquares(self, n):
        dp = [float('inf')] * (n + 1)
        dp[0] = 0 
        perfect_squares = [i * i for i in range(1, int(math.sqrt(n)) + 1)]
    
        for i in range(1, n + 1):
            for square in perfect_squares:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)
        return dp[n]