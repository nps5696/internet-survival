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

    def delNode(self, node):
        self.visual.remove(node)

    def visualize(self):
        G = nx.Graph()
        #G.add_nodes_from(self.nodes)
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()

class Graph():
    def __init__(self):
        self.edges = {}
        #self.costs =

    def add_edges(self, graph_ui, graph_items): #node_1, node_2, cost):
        for node in graph_items:

            # if node doesn't exist create one as dict of lists
            if node[0] != '' and node[1] != '':
                graph_ui.addEdge(node[0], node[1])

                if node[0] not in self.edges:
                    self.edges[node[0]] = []

                if node[1] not in self.edges:
                    self.edges[node[1]] = []

            # call graph ui to populate node
            graph_ui.addEdge(node[0], node[1])

            # attach nodes make an edge biderectional since graph is undirected
            self.edges[node[0]].append((node[1], node[2]))
            self.edges[node[1]].append((node[0], node[2]))

    def delete_node(self, node):
        if self.edges[node]:
            del self.edges[node]
            return 0
        else:
            print("Node was not found!")
            return 1

    def print_graph(self):
        # print all nodes and edges with weight, nodes are dict. keys and edges with weights are tuples
        for key,value in self.edges.items():
            print("node: " + str(key) + " , edges: " + str(value[::1]) )



# has to be separate function
def dijkst(graph, node_a, node_b):

    print("Find path between node A: " + str(node_a) + \
          " and node B: " + str(node_b))

    # TODO Dijkstra algorithm
    path = {node_a: (None, 0)}
    cur_node = node_a
    visited_node = set()

    while cur_node != node_b:
        visited_node.add(cur_node)
        cur_node_neighbours = graph.edges[cur_node]
        cost_to_cur_node = path[cur_node][1]

        for node in cur_node_neighbours:
            cost = graph.cost


if __name__ == '__main__':

    graph_items = [
        ['Chicago', 'Clevelend', 10],
        ['Chicago', 'Indianapolis', 10],
        ['Indianapolis', 'Cincinnati', 10],
        ['Seattle', 'Portland', 7],
        ['Seattle', 'Salt Lake City', 13],
        ['Portland', 'Sacramento', 9],
        ['Portland', 'Salt Lake City', 12],
        ['Sacramento', 'San Fransisco', 2],
        ['Sacramento', 'Fresno', 3],
        ['Sacramento', 'Salt Lake City', 5],
        ['San Francisco', 'San Jose', 1],
        ['San Jose', 'Santa Barbara', 4],
        ['Santa Barbara', 'Fresno', 3],
        ['Santa Barbara', 'Las Vegas', 2],
        ['Santa Barbara', 'Los Angeles', 0.5],
        ['Santa Barbara', 'Phoenix', 4],
        ['Los Angeles', 'San Diego', 0.6],
        ['San Diego', 'Phoenix', 4],
        ['Salt Lake City', 'Denver', 5],
        ['Salt Lake City', 'Colorado Springs', 6],
        ['Phoenix', 'Tucson', 1],
        ['Las Vegas', 'Tucson', 3],
        ['Colorado Springs', 'Santa Fe', 3],
        ['Santa Fe', 'El Paso', 2],
        ['Denver', 'Lincoln', 4],
        ['Colorado Springs', 'Topeka', 5],
        ['Colorado Springs', 'Amarillo', 3],
        ['Colorado Springs', 'Lubbock', 4.5],
        ['Amarillo', 'Lubbock', 1],
        ['El Paso', 'Amarillo', 5],
        ['Lubbock', 'Odessa', 1.3],
        ['Lubbock', 'Dallas', 3],
        ['Odessa', 'Dallas', 2],
        ['El Paso', 'Dallas', 3],
        ['El Paso', 'San Antonio', 4],
    ]



    # init graph UI
    graph_ui = GraphVisualization()
    # init graph datastructure
    G = Graph()
    # populate graph with edges and nodes
    G.add_edges(graph_ui, graph_items)

    G.print_graph()
    print("--------------- Updated Graph ---------------")
    G.delete_node('Dallas')
    G.print_graph()

    # find path between to nodes
    # TODO dijkst(G, "Portland", "Fresno")

    # TODO call func to remove a node
    # TODO rerun dijkst func


    # must be the last func, can be commented out while testing logic, this is for final demonatration
    graph_ui.visualize()
