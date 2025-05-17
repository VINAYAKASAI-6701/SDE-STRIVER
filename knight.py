from collections import deque

class Solution:
    def minStepToReachTarget(self, knightPos, targetPos, n):
        # All 8 possible knight moves
        directions = [
            (1, 2), (2, 1), (2, -1), (1, -2),
            (-1, -2), (-2, -1), (-2, 1), (-1, 2)
        ]
        
        # Convert 1-based to 0-based coordinates
        st_x, st_y = knightPos[0] - 1, knightPos[1] - 1
        end_x, end_y = targetPos[0] - 1, targetPos[1] - 1

        if st_x == end_x and st_y == end_y:
            return 0

        vis = [[False]*n for _ in range(n)]
        q = deque()
        q.append((st_x, st_y, 0))
        vis[st_x][st_y] = True

        while q:
            x, y, steps = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not vis[nx][ny]:
                    if nx == end_x and ny == end_y:
                        return steps + 1
                    vis[nx][ny] = True
                    q.append((nx, ny, steps + 1))

        return -1
