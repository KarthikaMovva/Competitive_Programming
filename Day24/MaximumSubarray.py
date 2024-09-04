class Solution(object):
    def maxSubArray(self, nums):
        presentsum =  nums[0]
        arrsum=nums[0]
        
        for i in range(1, len(nums)):
            presentsum = max(nums[i], presentsum + nums[i])
            if presentsum > arrsum:
                arrsum = presentsum
        
        return arrsum