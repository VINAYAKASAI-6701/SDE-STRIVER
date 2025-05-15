from collections import deque
class Solution:

    #Function to find distance of nearest 1 in the grid for each cell.
	def nearest(self, grid):
		#Code here
		#we are doing problem by reverse mapping finding 1 and finding nearest is any zeero to all its 4 dir so that 
		#dist for that 0 wll be 1
	
		row=len(grid)
		col=len(grid[0])
		#we dont want to tamper the data so create a vis matrix
        vis=[[0]*col for _ in range(row)]
        #we need a dist matrix to store nearest distance 
        dist=[[0]*col for _ in range(row)]
        q=deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    #push them into queue with dist as 0
                    #as we are doing reverse mapping we want 1 to be pushed first
                    q.append(((i,j),0))
                    vis[i][j]=1
                else:
                    vis[i][j]=0
        dir=[[1,0],[0,1],[-1,0],[0,-1]]
        while q:
            (r,c),dis=q.popleft()
            dist[r][c]=dis
            for dr,dc in dir:
                nr,nc=dr+r,dc+c
                if 0<=nr<row and 0<=nc<col and not vis[nr][nc]:
                    vis[nr][nc]=1
                    q.append(((nr,nc),dis+1))
        return dist
                