from basicgraph import read_graph, adjacent

def robot_path(graph, node):
    pass

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
