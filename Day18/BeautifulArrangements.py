class Solution(object):
    def countArrangement(self, n):
        def backtrack(pos, visited):
            if pos > n:
                return 1
        
            count = 0
            for num in range(1, n + 1):
                if not visited[num] and (num % pos == 0 or pos % num == 0):
                    visited[num] = True
                    count += backtrack(pos + 1, visited)
                    visited[num] = False
            return count
    
        visited = [False] * (n + 1)
        return backtrack(1, visited)
        
        