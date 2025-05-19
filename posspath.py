class Solution:
    
    def solve(self, curr, dest, adj):
        if curr == dest:
            return 1
        res = 0
        for nei in adj[curr]:
            res += self.solve(nei, dest, adj)
        return res
            
    def countPaths(self, V, adj, source, destination):
        return self.solve(source, destination, adj)
