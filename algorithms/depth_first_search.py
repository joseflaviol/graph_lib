class DFS:

    def __init__(self, G):
        self.G = G 
        self.visited = [False] * G.nV 
        self.components = 0

    def dfs(self):
        for v in range(self.G.nV):
            if not self.visited[v]:
                self.components += 1
                self.dfs_visit(v)

    def dfs_visit(self, u):
        self.visited[u] = True 

        for v in self.G.adj(u):
            if not self.visited[v]:
                self.dfs_visit(v)
