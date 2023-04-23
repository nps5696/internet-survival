####
# PSU, Final Project - Internet Survival
# Developers:
####

import networkx as nx
import matplotlib.pyplot as plt
import heapq
from collections import defaultdict

class GraphVisualization:

    def __init__(self):
        self.visual = []
        self.nodes = []

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
        G.add_nodes_from(self.nodes)
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()

class Graph():
    def __init__(self):
        self.edges = {}

    def add_edges(self, graph_ui, graph_items):
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
        # remove node itself
        if self.edges[node]:
            del self.edges[node]
        else:
            print("Node was not found!")
            return 1
        # remove vetrices to the node
        for key, values in self.edges.items():
            #print("key: " + str(key) + " values: " + str(values))
            edge_number = 0
            for value in values:
                #print("searching for value " + node + " in: " + str(value))
                if value[0] == node:
                    #print("deleting edge: " + str(value))
                    del self.edges[key][edge_number]
                    edge_number +=1
        return 0


    def get_node_neighbours(self, node):
        if self.edges[node]:
            return self.edges[node]
        else:
            print("Node was not found!")
            return 1

    def print_graph(self):
        # print all nodes and edges with weight, nodes are dict. keys and edges with weights are tuples
        for key,value in self.edges.items():
            print("node: " + str(key) + " , edges: " + str(value[::1]) )


# has to be separate function
def dijkst(graph, start, end):
    # Creates a dictionary to hold the distances
    distances = {key: float('inf') for key, value in graph.edges.items()}
    distances[start] = 0

    previous_vertices = {key: None for key, value in graph.edges.items()}

    # Creates a priority queue to store the vertices to visit next, ordered by their tentative distances
    priority_queue = [(0, start)]

    while len(priority_queue) > 0:
        curr_distance, curr_vertex = heapq.heappop(priority_queue)

        # Ignores the vertex if a shorter path is found
        if curr_distance > distances[curr_vertex]:
            continue

        # For each neighbor of the current vertex, it calculates the distance and updates the dictionaries

        # find neighbours
        curr_neighbors = graph.get_node_neighbours(curr_vertex)

        for neighbor, weight in curr_neighbors:
            distance = curr_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = curr_vertex
                # Stores the distance of the city and the neighbor nodes of the city
                heapq.heappush(priority_queue, (distance, neighbor))

    shortest_path = []
    current_vertex = end
    # Loops through the previous vertices and adds them to the shortest_path list to keep track of the path
    while current_vertex is not None:
        shortest_path.insert(0, current_vertex)
        current_vertex = previous_vertices[current_vertex]

    # Return the distances and shortest path as a tuple
    return distances[end], shortest_path


if __name__ == '__main__':

    graph_items = [
        ['Chicago', 'Clevelend', 10],
        ['Chicago', 'Indianapolis', 10],
        ['Indianapolis', 'Cincinnati', 10],
        ['Seattle', 'Portland', 7],
        ['Seattle', 'Salt Lake City', 13],
        ['Portland', 'Sacramento', 9],
        ['Portland', 'Salt Lake City', 12],
        ['Sacramento', 'San Francisco', 2],
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

    # # Converts list to a dictionary of dictionaries
    # graph = {}
    # for source, destination, cost in graph_items:
    #     if source not in graph:
    #         graph[source] = {}
    #     if destination not in graph:
    #         graph[destination] = {}
    #     graph[source][destination] = cost
    #     graph[destination][source] = cost


    # finds a path between two nodes
    #print("Path between two cities: " + str(dijkst(G, "Cincinnati", "Clevelend")))
    G.delete_node("Chicago")
    #G.print_graph()
    print('Path between two cities: ' + str(dijkst(G, "Cincinnati", "Clevelend")))


    # TODO call func to remove a node
    # TODO rerun dijkst func


    # must be the last func, can be commented out while testing logic, this is for final demonatration
    graph_ui.visualize()
