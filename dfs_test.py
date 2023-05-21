from graph.unweighted_graph import UnweightedGraph
from algorithms.depth_first_search import DFS

g = UnweightedGraph(5)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(3, 4)

dfs = DFS(g)
dfs.run()

print(dfs.opening_time)
print(dfs.closing_time)
print(dfs.components)

