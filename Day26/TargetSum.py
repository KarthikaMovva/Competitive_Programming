class Solution(object):
    def findTargetSumWays(self, nums, target):
         total = sum(nums)
         if total < abs(target) or (total + target) % 2 == 1:
            return 0
    
         subset = (total + target) // 2
         dp = [0] * (subset + 1)
         dp[0] = 1
    
         for num in nums:
             for j in range(subset, num - 1, -1):
                 dp[j] += dp[j - num]
    
         return dp[subset]