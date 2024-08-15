class Solution(object):
    def maxSubArray(self, nums):
        presentmax = arraymax = nums[0]
        
        for i in range(1, len(nums)):
            presentmax = max(nums[i], presentmax + nums[i])
            if presentmax > arraymax:
                arraymax = presentmax
        
        return arraymax
        