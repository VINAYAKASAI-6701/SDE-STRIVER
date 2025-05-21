class Solution:
    def topodfs(self, node, adj, vis, st):
        vis[node] = True
        for nei in adj[node]:
            if not vis[nei]:
                self.topodfs(nei, adj, vis, st)
        st.append(node)

    def topoSort(self, V, edges):
        vis = [False] * V
        adj = [[] for _ in range(V)]

        # Only u -> v (directed graph)
        for u, v in edges:
            adj[u].append(v)

        st = []
        for i in range(V):
            if not vis[i]:
                self.topodfs(i, adj, vis, st)

        return st[::-1]  # reverse to get correct topological order
