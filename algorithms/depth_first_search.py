class DFS:

    def __init__(self, G):
        self.G = G 
        self.visited = [False] * G.nV 
        self.components = 0
        self.parent = [None] * G.nV
        self.opening_time = {x: 0 for x in range(G.nV)}
        self.closing_time = {x: 0 for x in range(G.nV)}
        #self.run()

    def run(self):
        self.dfs()

    def dfs(self):
        self.time = 0
        for v in range(self.G.nV):
            if not self.visited[v]:
                self.components += 1
                self.dfs_visit(v)

    def dfs_visit(self, u):
        self.time += 1
        self.opening_time[u] = self.time
        self.visited[u] = True 

        for v in self.G.adj(u):
            if not self.visited[v]:
                self.parent[v] = u
                self.dfs_visit(v)

        self.time += 1
        self.closing_time[u] = self.time