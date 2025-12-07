from basicgraph import read_graph, random_node
from lab2exercise5 import bfs

def radius(graph):
    pass

def main():
    filepath = input("Enter the file path: ")
    graph = read_graph(filepath)
    print("radius is", radius(graph))

if __name__ == "__main__":
    main()
