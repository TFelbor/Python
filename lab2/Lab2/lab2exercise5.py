from basicgraph import read_graph, adjacent

def bfs(graph, node):
    pass

def display_path(pred, node):
    pass

def _get_node(graph):
    while True:
        node = input("Enter node: ")
        if node in graph:
            return node
        print(node, "is not a valid node")

def main():
    filepath = input('Enter file path: ')
    graph = read_graph(filepath)
    node = _get_node(graph)
    pred, dist = bfs(graph, node)
    print("distance from node", node, ":")
    print(dist)
    print("predecessor from node", node, ":")
    print(dist)
    target = _get_node(graph)
    print("Path from", node, "to", target, ":")
    display_path(pred, target)

if __name__ == "__main__":
    main()
