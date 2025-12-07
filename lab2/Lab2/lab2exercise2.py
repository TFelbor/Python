from basicgraph import *

def is_connected(graph):

    # Empty graph is considered a connected one
    if not graph:
        return True

    # Initiate the list for the visited vertices
    visited = []

    # Define the DFS function
    def DFS(graph, vertex):

        # Mark the current vertex as visited
        visited.append(vertex)

         # Get the adjacent nodes of the current vertex
        adjacent_nodes = adjacent(graph, vertex)

        # Recursively visit the adjacent nodes
        for adj in adjacent_nodes:
            if adj not in visited:
                DFS(graph, adj)

    # start DF from the first vertex in the graph
    start_vertex = next(iter(graph))
    DFS(graph, start_vertex)
    return len(visited) == len(graph)


def main():
    filepath = input("Enter the file path: ")
    graph = read_graph(filepath)
    print(graph)
    if is_connected(graph):
        print("Graph is connected")
    else:
        print("Graph is not connected")


if __name__ == "__main__":
    main()
