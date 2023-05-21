class UnweightedGraph:

    def __init__(self, nV, oriented = False):
        self.nV = nV
        self.oriented = oriented
        self.adj_list = []

        for _ in range(nV):
            self.adj_list.append([])
    
    def add_edge(self, u, v):
        self.adj_list[u].append(v)

        if not self.oriented:
            self.adj_list[v].append(u)    
    
    def adj(self, u):
        return self.adj_list[u]