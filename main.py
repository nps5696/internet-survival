####
# PSU, Final Project - Internet Survival
# Developers:
####


def add_edge(graph, node_1, node_2, cost):
    if node_1 not in graph:
        graph[node_1] = []

    if node_2 not in graph:
        graph[node_2] = []

    #attach nodes make an edge biderectional since graph is undirectd
    graph[node_1].append(node_2)
    graph[node_2].append(node_1)


def print_graph(graph):
    for key, value in graph.items():
        print("node: " + str(key) + " , edge: " + str(value))

def make_graph():
    graph = dict()

    add_edge(graph, 'Chicago', 'Clevelend', 10)
    add_edge(graph, 'Chicago', 'Indianapolis', 10)
    add_edge(graph, 'Indianapolis', 'Cincinnati', 10)

    print_graph(graph)




if __name__ == '__main__':
    make_graph()
