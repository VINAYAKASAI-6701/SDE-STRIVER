from collections import deque
class Solution:
	def orangesRotting(self, mat):
		#Code here
		row=len(mat)
		col=len(mat[0])
		fresh=0
		q=deque()
		for i in range(row):
		    for j in range(col):
		        if mat[i][j]==1:
		            fresh+=1
		        elif mat[i][j]==2:
		            q.append((i,j))
		 
        time=0
        dir=[[0,1],[1,0],[0,-1],[-1,0]]
        while q and fresh>0:
            for i in range(len(q)):
                r,c=q.popleft()
                for dr,dc in dir:
                    nr,nc=dr+r,dc+c
                    if 0<=nr<row and 0<=nc<col and mat[nr][nc]==1:
                        fresh-=1
                        mat[nr][nc]=2
                        q.append((nr,nc))
            time+=1
        return time if fresh==0 else -1
                