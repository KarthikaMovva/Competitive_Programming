class Solution(object):
    def nextGreaterElement(self, n):
        d = list(str(n))
        l = len(d)
        i = l - 2
        while i >= 0 and d[i] >= d[i + 1]:
            i -= 1
        if i == -1:
            return -1
        j = l - 1
        while d[j] <= d[i]:
            j -= 1
        d[i], d[j] = d[j], d[i]
        d = d[:i + 1] + d[i + 1:][::-1]
        num = int(''.join(d))
        return num if num <= 2**31 - 1 else -1