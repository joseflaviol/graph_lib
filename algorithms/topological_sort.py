from .depth_first_search import DFS

class TopologicalSort:

    def __init__(self, G):
        self.G = G 
        if self.G.oriented:
            self.dfs = DFS(G)
            self.dfs.run()
            self.order = sorted(self.dfs.closing_time, key = self.dfs.closing_time.get, reverse = True)

    def get_order(self):
        if self.G.oriented:
            return self.order
        return None