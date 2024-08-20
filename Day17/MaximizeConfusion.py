class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        def maxConsecutive(char):
            left, right = 0, 0
            maximumlen = 0
            count = 0
            
            while right < len(answerKey):
                if answerKey[right] != char:
                    count += 1
                
                while count > k:
                    if answerKey[left] != char:
                        count -= 1
                    left += 1
                
                maximumlen = max(maximumlen, right - left + 1)
                right += 1
                
            return maximumlen
        
        return max(maxConsecutive('T'), maxConsecutive('F'))
        