from collections import deque
class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        # code here
        v=len(adj)
        vis=[False]*v
        q=deque()
        bfs=[]
        q.append(0)
        vis[0]=True
        while q:
            node=q.popleft()
            bfs.append(node)
            for nei in adj[node]:
                if not vis[nei]:
                    q.append(nei)
                    vis[nei]=True
        return bfs
