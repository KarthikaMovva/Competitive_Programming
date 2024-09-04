class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        l=[]
        r=[]
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                l.append([arr[i],arr[j]])
                r.append(arr[i]/float(arr[j]))
        d=dict(zip(r,l))
        r.sort()
        return (d[r[k-1]])