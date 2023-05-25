class FloydWarshall:

    def __init__(self, G):
        self.G = G
        self.distances = []
        self.predecessors = [] 
        
        for i in range(G.nV):
            self.distances.append([])
            self.predecessors.append([])
            for j in range(G.nV):
                self.distances[i].append(0)
                self.predecessors[i].append(None)
        
        for i in range(G.nV):
            for j in range(i + 1, G.nV):
                
                if j not in G.adj(i):
                    self.distances[i][j] = float('inf') # idea: if and edge (i, j) doesnt exist, the distance between i and j is initialized as a very big number
                else:
                    self.distances[i][j] = G.weight(i, j)
                
                self.distances[j][i] = self.distances[i][j]
                self.predecessors[i][j] = i
                self.predecessors[j][i] = j  
            
        self.calculate()

    def calculate(self):
        for i in range(self.G.nV):
            for j in range(self.G.nV):
                for k in range(j + 1, self.G.nV):
                    if self.distances[j][i] + self.distances[i][k] < self.distances[j][k]:
                        self.distances[j][k] = self.distances[j][i] + self.distances[i][k]     
                        self.distances[k][j] = self.distances[j][k]
                        self.predecessors[j][k] = self.predecessors[i][k]
                        self.predecessors[k][j] = self.predecessors[i][j]

    def show_path(self, u, v):
        if u != v:
            self.show_path(u, self.predecessors[u][v])
        print("%d " % (v), end = ' ')