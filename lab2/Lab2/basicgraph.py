import random

def read_graph(filename):
    try:
        # Read the lines from the file one at a time
        with open(filename, "r") as file:
            lines = file.readlines()

            # Initialize empty graph variable
            graph = {}

            # Split + clean-up each line, then populate the dict with it
            for line in lines:
                dictEntry = line.split(":")
                dictEntry[1] = dictEntry[1].replace("\n", "")
                graph.update({dictEntry[0]: dictEntry[1]})

            # Return the constructed graph
            return graph

    # Error Handling
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return {}
    except Exception as e:
        print(f"Error reading file {filename}: {e}")
        return {}


def adjacent(graph, node):

    # Return empty list if graph is None or node not in graph
    if graph is None or node not in graph:
        return []

    # Retrieve the adjacent nodes to the vertex
    adjacentNodes = graph[node]

    # Turn the string of adjacent nodes into an iter by splitting on coma
    iter = adjacentNodes.split(",")
    return iter


def random_node(graph):

    # Return None if graph is None or empty
    if graph is None or len(graph) == 0:
        return None

    # Return a random node from the graph
    randomNode = random.choice(list(graph.keys()))
    return randomNode


def main():
    filepath = input("Enter file path: ")
    graph = read_graph(filepath)
    print(
        "-----------------------------------------------------------------------------------------------------"
    )
    print("Constructed Graph from '", filepath, "':\n", graph)
    v = random_node(graph)
    print("A Random Node:", v)
    print("The Adjacent Nodes Of ", v, ": ", end="")
    for a in adjacent(graph, v):
        print(a, end=" ")
    print(
        "\n-----------------------------------------------------------------------------------------------------"
    )

if __name__ == "__main__":
    main()
