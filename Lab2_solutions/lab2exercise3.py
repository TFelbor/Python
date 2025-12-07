from basicgraph import read_graph, adjacent

def is_acyclic(graph):
    visited = set()
    for node in graph:
        if node not in visited:
            if _cyclic(graph, visited, node):
                return False
    return True

def _cyclic(graph, visited, node, parent=None):
    visited.add(node)
    for a in adjacent(graph, node):
        if a == parent:
            continue
        if a in visited or _cyclic(graph, visited, a, node):
            return True
    return False

def main():
    filepath = input("Enter the file path: ")
    graph = read_graph(filepath)
    if is_acyclic(graph):
        print("Cyclic graph")
    else:
        print("Non-acyclic graph")

if __name__ == "__main__":
    main()

