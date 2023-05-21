class EdgeWeightedGraph:

    def __init__(self, nV, oriented = False):
        self.nV = nV
        self.oriented = oriented
        self.adj_list = []

        for _ in range(nV):
            self.adj_list.append({})
    
    def add_edge(self, u, v, w)
        self.adj_list[u][v] = w 

        if not self.oriented:
            self.adj_list[v][u] = w 
    
    def adj(self, u):
        return list(self.adj_list[u].keys())
    
    def weight(self, u, v):
        return self.adj_list[u][v]