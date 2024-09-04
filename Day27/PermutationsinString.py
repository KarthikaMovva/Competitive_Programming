from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        len1, len2 = len(s1), len(s2)
    
        if len1 > len2:
            return False
    
        s1Count = Counter(s1)
        windowCount = Counter(s2[:len1])
    
        if s1Count == windowCount:
            return True
    
        for i in range(len1, len2):
            windowCount[s2[i]] += 1 
            windowCount[s2[i - len1]] -= 1  
        
            if windowCount[s2[i - len1]] == 0:
                del windowCount[s2[i - len1]]
        
            if s1Count == windowCount:
                return True
    
        return False