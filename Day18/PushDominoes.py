class Solution(object):
    def pushDominoes(self, dominoes):
        n = len(dominoes)
        pushes = [0] * n
        forcetopush = 0
        for i in range(n):
            if dominoes[i] == 'R':
                forcetopush = n  
            elif dominoes[i] == 'L':
                forcetopush = 0
            else:
                forcetopush = max(forcetopush - 1, 0)
            pushes[i] += forcetopush
   
        forcetopush = 0
        for i in range(n-1, -1, -1):
            if dominoes[i] == 'L':
                forcetopush = n  
            elif dominoes[i] == 'R':
                forcetopush = 0
            else:
                forcetopush = max(forcetopush - 1, 0)
            pushes[i] -= forcetopush
        arr = []
        for f in pushes:
            if f > 0:
                arr.append('R')
            elif f < 0:
                arr.append('L')
            else:
                arr.append('.')
    
        return ''.join(arr)

        