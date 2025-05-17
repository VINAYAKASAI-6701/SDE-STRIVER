class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def bt(self,node,adj,vis,dfs):
        vis[node]=True
        dfs.append(node)
        for nei in adj[node]:
            if not vis[nei]:
                self.bt(nei,adj,vis,dfs)
        
    def dfs(self, adj):
        # code here
        n=len(adj)
        vis=[False]*n
        dfs=[]
        start=0
        self.bt(start,adj,vis,dfs)
        return dfs
