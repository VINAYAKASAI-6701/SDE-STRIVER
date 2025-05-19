from collections import deque
class Solution:
    
    #Function to find whether a path exists from the source to destination.
	def is_Possible(self, grid):
		#Code here
		n=len(grid)
		dir=[[0,1],[1,0],[0,-1],[-1,0]]
		vis=[[False]*n for _ in range(n)]
		q=deque()
		for i in range(n):
		    for j in range(n):
		        if grid[i][j]==1:
		            q.append((i,j))
		            vis[i][j]=True
		            break
		            
	   
		
		while q:
		    r,c=q.popleft()
		    for dr,dc in dir:
		        nr,nc=dr+r,dc+c
		        if 0 <= nr < n and 0 <= nc < n and not vis[nr][nc] and grid[nr][nc] != 0:
		            vis[nr][nc]=True
		            if grid[nr][nc]==2:
		                return 1
		            q.append((nr,nc))
		            
		return 0