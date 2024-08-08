from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        l=len(nums)
        if k>l:
            return []
        else:
            dq=deque()
            for i in range(k):
                while dq and nums[dq[-1]]<nums[i]:
                    dq.pop()
                dq.append(i)
            maximum=[nums[dq[0]]]
            for i in range(k,l):
                if dq and dq[0]==i-k:
                    dq.popleft()
                while dq and nums[dq[-1]]<nums[i]:
                    dq.pop()
                dq.append(i)
                maximum.append(nums[dq[0]])
            return maximum