import dis
from basicgraph import *

def BFS_cycle(graph, start_vertex):

    # Initialize necessary variables
    visited = set()
    queue = []
    parent = {}

    # Start BFS
    visited.add(start_vertex)
    queue.append(start_vertex)

    while(queue):

        # Dequeue
        current_vertex = queue.pop(0)

        # Check all neighbors of the current vertex
        adjacents = adjacent(graph, current_vertex)
        for neighbor in adjacents:

            # IF neighbor hasn't been visited yet
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current_vertex
                queue.append(neighbor)

            # If neighbor is already visited and is not the parent
            elif neighbor in visited and parent.get(current_vertex) != neighbor:

                return True  # Cycle detected

    return False  # No cycle found

def is_acyclic(graph):
    graphSize = len(graph)
    bools = set()
    for vertex in graph:
        bools.add(BFS_cycle(graph, vertex))
    if True in bools:
        return False
    else:
        return True

def main():
    filepath = input("Enter the file path: ")
    graph = read_graph(filepath)
    if is_acyclic(graph):
        print("Acyclic graph")
    else:
        print("Cyclic graph")

if __name__ == "__main__":
    main()
