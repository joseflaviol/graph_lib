from graph.unweighted_graph import UnweightedGraph
from algorithms.breadth_first_search import BFS

g = UnweightedGraph(9)

g.add_edge(0, 1)
g.add_edge(0, 3)
g.add_edge(0, 8)
g.add_edge(1, 2)
g.add_edge(3, 2)
g.add_edge(4, 3)
g.add_edge(4, 6)
g.add_edge(5, 4)
g.add_edge(5, 6)
g.add_edge(7, 6)

bfs = BFS(g)
bfs.run()

print(bfs.level)

