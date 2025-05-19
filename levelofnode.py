User function Template for python3
from collections import deque
class Solution:
    
    #Function to find the level of node X.
    def nodeLevel(self, V, adj, X):
        # code here
        q=deque()
        vis=[False]*V
        q.append((0,0))
        vis[0]=True
        while q:
            node,steps=q.popleft()
            for nei in adj[node]:
                if nei==X:
                    return steps+1
                elif not vis[nei]:
                    q.append((nei,steps+1))
                    vis[nei]=True
        return -1