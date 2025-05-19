from collections import deque

class Solution:
    def xShape(self, grid):
        row = len(grid)
        col = len(grid[0])
        vis = [[False] * col for _ in range(row)]
        q = deque()
        ans = 0
        dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 'X' and not vis[i][j]:
                    ans += 1
                    q.append((i, j))
                    vis[i][j] = True
                    while q:
                        r, c = q.popleft()
                        for dr, dc in dir:
                            nr, nc = r + dr, c + dc
                            if (
                                0 <= nr < row and 0 <= nc < col and
                                not vis[nr][nc] and grid[nr][nc] == 'X'
                            ):
                                q.append((nr, nc))
                                vis[nr][nc] = True
        return ans