class Solution(object):
    def maximizeGreatness(self, nums):
        nums.sort()
        length = len(nums)
        i, j = 0, 0
        greatnessValue = 0
    
        while i < length and j < length:
            if nums[j] > nums[i]:
                greatnessValue += 1
                i += 1
            j += 1
    
        return greatnessValue
        