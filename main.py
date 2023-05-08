####
# PSU, Final Project - Internet Survival
# Developers: Bryan Naroditskiy, Colin George, Nikolay Sizov
####

import sys
import networkx as nx
import matplotlib.pyplot as plt
import heapq
import random
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
            # print("Node for deletion was not found!") #debugging
            return 1
        # remove vetrices to the node
        for key, values in self.edges.items():
            # print("key: " + str(key) + " values: " + str(values)) #debugging
            edge_number = 0
            for value in values:
                # print("searching for value " + node + " in: " + str(values[edge_number]) + " checking city: " + str(values[edge_number][0])) #debugging
                if value[0] == node:
                    # print("deleting edge: " + str(self.edges[key][edge_number])) #debugging
                    del self.edges[key][edge_number]
                    edge_number -= 1
                edge_number += 1
        return 0

    def get_2_rand_nodes(self):
        nodes = [i for i in self.edges.keys()]
        rand_node_1 = random.choice(nodes)
        rand_node_2 = random.choice(nodes)
        while rand_node_1 == rand_node_2:
            #print("Matching nodes picked, regenerating..")
            rand_node_1 = random.choice(nodes)
            rand_node_2 = random.choice(nodes)

        return rand_node_1, rand_node_2

    def get_rand_node(self, node_1, node_2):
        # deleting node which is not start of end node
        nodes = [i for i in self.edges.keys()]
        rand_node = random.choice(nodes)
        while rand_node in [node_1, node_2]:

            # print("Start/End nodes picked, regenerating..")
            rand_node = random.choice(nodes)

        return rand_node

    def get_node_neighbors(self, node):
        if self.edges[node]:
            return self.edges[node]
        else:
            #print("Neighbor nodes not found!")
            return -1

    def print_graph(self):
        # print all nodes and edges with weight, nodes are dict. keys and edges with weights are tuples
        for key, value in self.edges.items():
            print("node: " + str(key) + " , edges: " + str(value[::1]))


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

        # find neighbors
        curr_neighbors = graph.get_node_neighbors(curr_vertex)
        # no neighbors found, exit control
        if curr_neighbors == -1:
            return -1, -1

        for neighbor, weight in curr_neighbors:
            distance = curr_distance + weight
            # no key found, node was just removed, exiting
            if neighbor not in distances.keys():
                return -1, -1
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
        ['Boston', 'New York', 215],
        ['Boston', 'Portland', 105],
        ['Boston', 'Montreal', 307],
        ['New York', 'Philadelphia', 94],
        ['New York', 'Baltimore', 188],
        ['New York', 'Boston', 215],
        ['Philadelphia', 'Baltimore', 102],
        ['Philadelphia', 'Washington D.C.', 142],
        ['Baltimore', 'Washington D.C.', 38],
        ['Montreal', 'Ottawa', 201],
        ['Ottawa', 'Toronto', 269],
        ['Toronto', 'Detroit', 279],
        ['Toronto', 'Buffalo', 105],
        ['Detroit', 'Chicago', 283],
        ['Chicago', 'Milwaukee', 89],
        ['Chicago', 'Indianapolis', 182],
        ['Chicago', 'St. Louis', 297],
        ['Milwaukee', 'Minneapolis', 337],
        ['Minneapolis', 'St. Paul', 11],
        ['St. Paul', 'Fargo', 267],
        ['Fargo', 'Bismarck', 191],
        ['Bismarck', 'Billings', 428],
        ['Billings', 'Spokane', 464],
        ['Spokane', 'Seattle', 279],
        ['Seattle', 'Portland', 173],
        ['Portland', 'San Francisco', 634],
        ['San Francisco', 'Los Angeles', 382],
        ['Los Angeles', 'San Diego', 124],
        ['San Diego', 'Phoenix', 355],
        ['Phoenix', 'Albuquerque', 421],
        ['Albuquerque', 'Denver', 449],
        ['Denver', 'Salt Lake City', 370],
        ['Salt Lake City', 'Boise', 346],
        ['Boise', 'Helena', 429],
        ['Helena', 'Butte', 68],
        ['Butte', 'Spokane', 396],
        ['Spokane', 'Boise', 290],
        ['Salt Lake City', 'Las Vegas', 421],
        ['Las Vegas', 'Los Angeles', 435],
        ['Los Angeles', 'Phoenix', 373],
        ['Phoenix', 'Santa Fe', 483],
        ['Santa Fe', 'Oklahoma City', 543],
        ['Oklahoma City', 'Dallas', 206],
        ['Dallas', 'Houston', 239],
        ['Houston', 'New Orleans', 352],
        ['New Orleans', 'Mobile', 162],
        ['Mobile', 'Tallahassee', 204],
        ['Tallahassee', 'Atlanta', 225],
        ['Atlanta', 'Nashville', 250],
        ['Nashville', 'Louisville', 173],
        ['Louisville', 'Columbus', 204],
        ['Columbus', 'Pittsburgh', 185],
        ['Pittsburgh', 'Cleveland', 129],
        ['Cleveland', 'Detroit', 168],
        ['Detroit', 'Buffalo', 295],
        ['Buffalo', 'Rochester', 73]
    ]

    # init graph UI
    graph_ui = GraphVisualization()
    # init graph datastructure
    G = Graph()
    # populate graph with edges and nodes
    G.add_edges(graph_ui, graph_items)
    # func caller, avarage "node num failure" produced here
    fail_num_tracker = []

    while True:

        print("Choose an option below: ")
        print("1. Manually Choose Nodes")
        print("2. Network Survivabilty")
        print("3: Print Map")
        print("4. Exit ")

        user_input = input("Option: ")

        if user_input == '1':
            # Get two nodes from user
            node_1 = input("Enter the name of node 1: ")
            node_2 = input("Enter the name of node 2: ")

            # calculate the survivability
            dist, init_path = dijkst(G, node_1, node_2)

            # check for invalid nodes
            if dist == (-1, -1):
                print("Invalid nodes. Please enter valid nodes.")

            # print survivability
            else:
                print("The cost to travel of the internet traffic between city {0} and city {1} is {2}".format(
                    node_1, node_2, dist))
                # failing nodes here
                run_num = 0
                max_run_num = len(G.edges.keys())
                while dist != float('inf'):
                    if run_num > max_run_num:
                        #print("Neigboring nodes, not possible to disrupt network!")
                        break
                    node_for_deletion = G.get_rand_node(node_1, node_2)
                    # print("Deleting node: " + str(node_for_deletion)) #debugging
                    G.delete_node(node_for_deletion)

                    dist, path = dijkst(G, node_1, node_2)
                    # no neighbor found, no net. path possible
                    if dist == path == -1:
                        dist = float('inf')

                    # print("Network route between city: " + str(node_1) + " and " + node_2 + " is " + str(dist) + str(path)) #debugging
                    run_num += 1

                # print("Route : " + str(init_path) +
                # " unreachable after deleting last node: " + str(node_for_deletion))
                print(
                    "Number Of nodes deleted until network path unreachable: " + str(run_num))
                fail_num_tracker.append(run_num)

        if user_input == '2':
            for i in range(1000):

                G = Graph()
                # populate graph with edges and nodes
                G.add_edges(graph_ui, graph_items)
                # pick two random nodes for network route planning
                node_1, node_2 = G.get_2_rand_nodes()

                dist, init_path = dijkst(G, node_1, node_2)
                run_num = 0
                max_run_num = len(G.edges.keys())
                while dist != float('inf'):
                    if run_num > max_run_num:
                        #print("Neigboring nodes, not possible to disrupt network!")
                        break
                    node_for_deletion = G.get_rand_node(node_1, node_2)
                    # print("Deleting node: " + str(node_for_deletion)) #debugging
                    G.delete_node(node_for_deletion)

                    dist, path = dijkst(G, node_1, node_2)
                 # no neighbor found, no net. path possible
                    if dist == path == -1:
                        dist = float('inf')

                # print("Network route between city: " + str(node_1) + " and " + node_2 + " is " + str(dist) + str(path)) #debugging
                    run_num += 1

                #print("Route : " + str(init_path) + " unreachable after deleting last node: " + str(node_for_deletion))
                #print("Number Of nodes deleted until network path unreachable: " + str(run_num))
                fail_num_tracker.append(run_num)

            print(
                "###########################################################################")
            print("Nodes deleted until network failure occurred: " + str(fail_num_tracker)
                  + "\nAverage number of nodes failures needed for network path to become unreachable: "
                  + str(int(sum(fail_num_tracker)/len(fail_num_tracker))))
            print(
                "###########################################################################")
        elif user_input == '3':
            graph_ui.visualize()
        elif user_input == '4':
            print("Thank you for using the program!")
            sys.exit()
