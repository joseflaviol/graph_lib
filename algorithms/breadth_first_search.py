class BFS:

    def __init__(self, G, source = 0):
        self.G = G 
        self.source = source
        self.marked = [False] * G.nV
        self.parent = [None] * G.nV
        self.level = [0] * G.nV
    
    def run(self):
        self.bfs()
    
    def bfs(self):
        self.marked[self.source] = True
        frontier = [self.source]

        while frontier:
            nxt = []
            for u in frontier:
                for v in self.G.adj(u):
                    if not self.marked[v]:
                        self.marked[v] = True
                        self.parent[v] = u
                        self.level[v] = self.level[u] + 1
                        nxt.append(v)
            frontier = nxt
