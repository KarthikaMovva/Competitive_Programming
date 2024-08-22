class Solution(object):
    def longestPalindrome(self, s):
        l = len(s)
        if l == 0:
            return ""
        mark = [[False] * l for _ in range(l)]
        start, max_length = 0, 1
        for i in range(l):
            mark[i][i] = True
        for i in range(l - 1):
            if s[i] == s[i + 1]:
                mark[i][i + 1] = True
                start = i
                max_length = 2
        for length in range(3, l+ 1):
            for i in range(l - length + 1):
                j = i + length - 1
                if s[i] == s[j] and mark[i + 1][j - 1]:
                    mark[i][j] = True
                    start = i
                    max_length = length
    
        return s[start:start + max_length]
        