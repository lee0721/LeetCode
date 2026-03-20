class Solution:
    cycle_start = -1
    
    def dfs(self, src, visited, adj_list, parent):
        visited[src] = True

        for adj in adj_list[src]:
            if not visited[adj]:
                parent[adj] = src
                self.dfs(adj, visited, adj_list, parent)
            elif adj != parent[src] and self.cycle_start == -1:
                self.cycle_start = adj
                parent[adj] = src
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        visited = [False] * N
        parent = [-1] * N

        adj_list = [[] for _ in range(N)]
        for edge in edges:
            adj_list[edge[0] - 1].append(edge[1] - 1)
            adj_list[edge[1] - 1].append(edge[0] - 1)

        self.dfs(0, visited, adj_list, parent)

        cycle_nodes = {}
        node = self.cycle_start

        while True:
            cycle_nodes[node] = 1
            node = parent[node]
            if node == self.cycle_start:
                break

        for i in range(len(edges) - 1, -1, -1):
            if (edges[i][0] - 1) in cycle_nodes and (edges[i][1] - 1) in cycle_nodes:
                return edges[i]
        return []