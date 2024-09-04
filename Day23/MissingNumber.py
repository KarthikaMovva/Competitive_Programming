class Solution(object):
    def firstMissingPositive(self, nums):
        length = len(nums)
        for i in range(length):
            while 1 <= nums[i] <= length and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(length):
            if nums[i] != i + 1:
                return i + 1
        return length + 1