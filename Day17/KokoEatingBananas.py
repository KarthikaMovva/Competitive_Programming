class Solution:
    def minEatingSpeed(self, piles, h):
        low, high = 1, 10**9
        while low <= high:
            k = (low + high) // 2
            totaltime = sum((pile + k - 1) // k for pile in piles)
            if totaltime > h: low = k + 1
            else: high = k - 1
        return low