from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        freshoranges = 0
    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    freshoranges += 1
    
        if freshoranges == 0:
            return 0
    
        time = -1
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
        while queue:
            time += 1
            for m in range(len(queue)):
                x, y = queue.popleft()
            
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
                        freshoranges -= 1
    
        return time if freshoranges == 0 else -1
        