####
# PSU, Final Project - Internet Survival
# Developers:
####

import networkx as nx
import matplotlib.pyplot as plt

class GraphVisualization:

    def __init__(self):

        self.visual = []
        #self.nodes = []

    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    def addNode(self, a):
        temp = [a]
        self.visual.append(temp)

    def visualize(self):
        G = nx.Graph()
        #G.add_nodes_from(self.nodes)
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()

def add_edge(graph_v, graph, node_1, node_2, cost):
    if node_1 != '' and node_2 != '':
        graph_v.addEdge(node_1, node_2)

        if node_1 not in graph:
            graph[node_1] = []

        if node_2 not in graph:
            graph[node_2] = []

    # attach nodes make an edge biderectional since graph is undirectd
    graph[node_1].append((node_2, cost))
    graph[node_2].append((node_1, cost))


def print_graph(graph):
    for key, value in graph.items():
        print("node: " + str(key) + " , edge: " + str(value))

def dijkst(graph, node_a, node_b):

    print("Find path between node A: " + str(node_a) + \
          " and node B: " + str(node_b))

    # TODO Dijkstra algorithm



def make_graph():
    # build graphical representation of the graph
    graph_v = GraphVisualization()
    # build graph
    graph = dict()

    add_edge(graph_v, graph, 'Chicago', 'Clevelend', 10)
    add_edge(graph_v, graph, 'Chicago', 'Indianapolis', 10)
    add_edge(graph_v, graph, 'Indianapolis', 'Cincinnati', 10)
    add_edge(graph_v, graph, 'Seattle', 'Portland', 7)
    add_edge(graph_v, graph, 'Seattle', 'Salt Lake City', 13)
    add_edge(graph_v, graph, 'Portland', 'Sacramento', 9)
    add_edge(graph_v, graph, 'Portland', 'Salt Lake City', 12)
    add_edge(graph_v, graph, 'Sacramento', 'San Fransisco', 2)
    add_edge(graph_v, graph, 'Sacramento', 'Fresno', 3)
    add_edge(graph_v, graph, 'Sacramento', 'Salt Lake City', 5)
    add_edge(graph_v, graph, 'San Francisco', 'San Jose', 1)
    add_edge(graph_v, graph, 'San Jose', 'Santa Barbara', 4)
    add_edge(graph_v, graph, 'Santa Barbara', 'Fresno', 3)
    add_edge(graph_v, graph, 'Santa Barbara', 'Las Vegas', 2)
    add_edge(graph_v, graph, 'Santa Barbara', 'Los Angeles', 0.5)
    add_edge(graph_v, graph, 'Santa Barbara', 'Phoenix', 4)
    add_edge(graph_v, graph, 'Los Angeles', 'San Diego', 0.6)
    add_edge(graph_v, graph, 'San Diego', 'Phoenix', 4)
    add_edge(graph_v, graph, 'Salt Lake City', 'Denver', 5)
    add_edge(graph_v, graph, 'Salt Lake City', 'Colorado Springs', 6)
    add_edge(graph_v, graph, 'Phoenix', 'Tucson', 1)
    add_edge(graph_v, graph, 'Las Vegas', 'Tucson', 3)
    add_edge(graph_v, graph, 'Colorado Springs', 'Santa Fe', 3)
    add_edge(graph_v, graph, 'Santa Fe', 'El Paso', 2)
    add_edge(graph_v, graph, 'Denver', 'Lincoln', 4)
    add_edge(graph_v, graph, 'Colorado Springs', 'Topeka', 5)
    add_edge(graph_v, graph, 'Colorado Springs', 'Amarillo', 3)
    add_edge(graph_v, graph, 'Colorado Springs', 'Lubbock', 4.5)
    add_edge(graph_v, graph, 'Amarillo', 'Lubbock', 1)
    add_edge(graph_v, graph, 'El Paso', 'Amarillo', 5)
    add_edge(graph_v, graph, 'Lubbock', 'Odessa', 1.3)
    add_edge(graph_v, graph, 'Lubbock', 'Dallas', 3)
    add_edge(graph_v, graph, 'Odessa', 'Dallas', 2)
    add_edge(graph_v, graph, 'El Paso', 'Dallas', 3)
    add_edge(graph_v, graph, 'El Paso', 'San Antonio', 4)

    print_graph(graph)

    # find path between to nodes
    dijkst(graph, "Portland", "Fresno")

    # TODO call func to remove a node
    # TODO rerun dijkst func

    # must be the last func, can be commented out while testing logic, this is for final demonatration
    graph_v.visualize()


if __name__ == '__main__':
    make_graph()
