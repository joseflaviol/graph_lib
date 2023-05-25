from graph.weighted_graph import EdgeWeightedGraph
from algorithms.floyd_warshall import FloydWarshall

g = EdgeWeightedGraph(4)

g.add_edge(0, 2, 5)
g.add_edge(0, 3, 1)
g.add_edge(2, 3, 1)
g.add_edge(3, 1, 2)

fw = FloydWarshall(g)

print(fw.distances)
fw.show_path(0, 1)
