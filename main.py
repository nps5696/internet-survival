####
# PSU, Final Project - Internet Survival
# Developers:
####


def add_edge(graph, node_1, node_2, cost):
    if node_1 not in graph:
        graph[node_1] = []

    if node_2 not in graph:
        graph[node_2] = []

    # attach nodes make an edge biderectional since graph is undirectd
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
    add_edge(graph, 'Seattle', 'Portland', 7)
    add_edge(graph, 'Seattle', 'Salt Lake City', 13)
    add_edge(graph, 'Portland', 'Sacramento', 9)
    add_edge(graph, 'Portland', 'Salt Lake City', 12)
    add_edge(graph, 'Sacramento', 'San Fransisco', 2)
    add_edge(graph, 'Sacramento', 'Fresno', 3)
    add_edge(graph, 'Sacramento', 'Salt Lake City', 5)
    add_edge(graph, 'San Francisco', 'San Jose', 1)
    add_edge(graph, 'San Jose', 'Santa Barbara', 4)
    add_edge(graph, 'Santa Barbara', 'Fresno', 3)
    add_edge(graph, 'Santa Barbara', 'Las Vegas', 2)
    add_edge(graph, 'Santa Barbara', 'Los Angeles', 0.5)
    add_edge(graph, 'Santa Barbara', 'Phoenix', 4)
    add_edge(graph, 'Los Angeles', 'San Diego', 0.6)
    add_edge(graph, 'San Diego', 'Phoenix', 4)
    add_edge(graph, 'Salt Lake City', 'Denver', 5)
    add_edge(graph, 'Salt Lake City', 'Colorado Springs', 6)
    add_edge(graph, 'Phoenix', 'Tucson', 1)
    add_edge(graph, 'Las Vegas', 'Tucson', 3)
    add_edge(graph, 'Colorado Springs', 'Santa Fe', 3)
    add_edge(graph, 'Santa Fe', 'El Paso', 2)
    add_edge(graph, 'Denver', 'Lincoln', 4)
    add_edge(graph, 'Colorado Springs', 'Topeka', 5)
    add_edge(graph, 'Colorado Springs', 'Amarillo', 3)
    add_edge(graph, 'Colorado Springs', 'Lubbock', 4.5)
    add_edge(graph, 'Amarillo', 'Lubbock', 1)
    add_edge(graph, 'El Paso', 'Amarillo', 5)
    add_edge(graph, 'Lubbock', 'Odessa', 1.3)
    add_edge(graph, 'Lubbock', 'Dallas', 3)
    add_edge(graph, 'Odessa', 'Dallas', 2)
    add_edge(graph, 'El Paso', 'Dallas', 3)
    add_edge(graph, 'El Paso', 'San Antonio', 4)

    print_graph(graph)


if __name__ == '__main__':
    make_graph()
