class Solution(object):
    def numMovesStonesII(self, stones):
        stones.sort()
        m=len(stones)
        max_moves=max(stones[-1]-stones[1],stones[-2]-stones[0])-(m-2)
        min_moves=float('inf')
        k=0
        for i in range(m):
            while k<m and stones[k]-stones[i]+1<=m:
                k+=1
            curr_window=k-i
            if curr_window==m-1 and stones[k-1]-stones[i]+1==m-1:
                min_moves=min(2,min_moves)
            else:
                min_moves=min(m-curr_window,min_moves)
        return[min_moves,max_moves]