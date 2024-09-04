class Solution(object):
    def longestConsecutive(self, nums):
        differentnums=set(nums)
        max_consec=0
        for h in nums:
            if h-1 not in differentnums:
                curr_len=0
                while h+curr_len in differentnums:
                    curr_len+=1
                max_consec=max(max_consec,curr_len)
        return max_consec