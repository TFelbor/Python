from basicgraph import *

def is_connected(graph):
    visited = set()
    _explore(graph, visited, random_node(graph))
    return len(visited) == len(graph)

def _explore(graph, visited, node):
    visited.add(node)
    for a in adjacent(graph, node):
        if a not in visited:
            _explore(graph, visited, a)

def main():
    filepath = input("Enter the file path: ")
    graph = read_graph(filepath)
    if is_connected(graph):
        print("Graph is connected")
    else:
        print("Graph is not connected")

if __name__ == "__main__":
    main()
