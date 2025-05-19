from collections import deque

class Solution:
    def numIslands(self, grid):
        row = len(grid)
        col = len(grid[0])
        vis = [[False]*col for _ in range(row)]
        islands = 0

        directions = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 'L' and not vis[i][j]:
                    islands += 1
                    q = deque()
                    q.append((i, j))
                    vis[i][j] = True
                    
                    while q:
                        r, c = q.popleft()
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < row and 0 <= nc < col and not vis[nr][nc] and grid[nr][nc] == 'L':
                                vis[nr][nc] = True
                                q.append((nr, nc))
        
        return islands