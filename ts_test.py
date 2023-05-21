from graph.unweighted_graph import UnweightedGraph
from algorithms.topological_sort import TopologicalSort

g = UnweightedGraph(9, oriented = True)

g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(0, 3)
g.add_edge(3, 2)
g.add_edge(4, 3)
g.add_edge(4, 6)
g.add_edge(5, 4)
g.add_edge(5, 6)
g.add_edge(7, 6)

ts = TopologicalSort(g)
print(ts.get_order())

