from basicgraph import read_graph, adjacent

def robot_path(graph, node):
    visited = set()
    _explore_path(graph, visited, node)

def _explore_path(graph, visited, node, parent=None):
    visited.add(node)
    for a in adjacent(graph, node):
        if a == parent:
            continue
        if a not in visited:
            print("go to", a)
            _explore_path(graph, visited, a, node)
            print("go to", node)

def main():
    filepath = input("Enter file path: ")
    graph = read_graph(filepath)
    while True:
        node = input("Enter node: ")
        if node in graph:
            break
        print(node, "is not a valid node")
    print()
    robot_path(graph, node)

if __name__ == "__main__":
    main()
