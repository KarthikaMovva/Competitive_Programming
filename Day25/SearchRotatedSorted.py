class Solution(object):
    def search(self, nums, target):
        start, end = 0, len(nums) - 1

        while start <= end:
            midpos = (start + end) // 2

            if nums[midpos] == target:
                return midpos
            if nums[start] <= nums[midpos]:
                if nums[start] <= target < nums[midpos]:
                    end = midpos - 1
                else:
                    start = midpos + 1
            else:
                if nums[midpos] < target <= nums[end]:
                    start = midpos + 1
                else:
                    end = midpos - 1

        return -1