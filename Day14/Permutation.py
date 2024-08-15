class Solution(object):
    def permute(self, nums):
        def possiblecombinations(firstnum):
            if firstnum==len(nums):
                array.append(nums[:])
                return
            else:
                for i in range(firstnum,len(nums)):
                    nums[firstnum],nums[i]=nums[i],nums[firstnum]
                    possiblecombinations(firstnum+1)
                    nums[firstnum],nums[i]=nums[i],nums[firstnum]
        array=[]
        possiblecombinations(0)
        return array


        