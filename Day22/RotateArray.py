class Solution(object):
    def rotate(self, nums, k):
        length = len(nums)
        k %= length  
        rotate = nums[-k:] + nums[:-k]
        nums[:] = rotate