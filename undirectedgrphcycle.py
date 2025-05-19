from typing import List
from collections import deque
class Solution:
    def bfs(self,src,adj,vis):
        vis[src]=True
        q=deque([(src,-1)])
        while q:
            node,parent=q.popleft()
            for nei in adj[node]:
                if not vis[nei]:
                    vis[nei]=True
                    q.append((nei,node))
                elif parent!=nei:
                    return True
        return False
    def isCycle(self, V,edges):
        adj=[[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        vis=[False]*V
        for i in range(V):
            if not vis[i]:
                if self.bfs(i,adj,vis):
                    return True
        return False
        #Code here



