from basicgraph import read_graph, random_node
from lab2exercise5 import bfs

def radius(graph):
    _ , dist = bfs(graph, random_node(graph))
    m = max(dist.items(), key=lambda x: x[1])
    _ , dist = bfs(graph, m[0])
    return max(dist.items(), key=lambda x: x[1])[1]

def main():
    filepath = input("Enter the file path: ")
    graph = read_graph(filepath)
    print("radius is", radius(graph))

if __name__ == "__main__":
    main()
