class Solution(object):
    def findJudge(self, n, trust):
        if n==1:
            return 1
        outgoing=[0]*(n+1)
        incoming=[0]*(n+1)
        for l,m in trust:
            outgoing[l]+=1
            incoming[m]+=1
        for i in range(1,n+1):
            if outgoing[i]==0 and incoming[i]==n-1:
                return i
        return -1