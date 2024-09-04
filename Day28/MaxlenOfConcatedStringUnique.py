class Solution(object):
    def maxLength(self, arr):
        def isdifferent(string):
            return len(string)==len(set(string))
        def Findmaxlen(i,formedstring):
            if not isdifferent(formedstring):
                return 0
            maximumlength=len(formedstring)
            for j in range(i,len(arr)):
                maximumlength=max(maximumlength,Findmaxlen(j+1,formedstring+arr[j]))
            return maximumlength
        return Findmaxlen(0,"")