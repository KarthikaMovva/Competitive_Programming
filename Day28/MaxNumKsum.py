class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()
        l,r=0,len(nums)-1
        operate=0
        while l<r:
            sum_value=nums[l]+nums[r]
            if sum_value==k:
                l+=1
                r-=1
                operate+=1
            elif sum_value<k:
                l+=1
            else:
                r-=1
        return operate