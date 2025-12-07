from basicgraph import read_graph, adjacent
from stack import Stack

def dfsit(graph, node):
    visited = set()
    stack = Stack()
    stack.push(node)
    while not stack.is_empty():
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node,"was just visited")
            for a in adjacent(graph, node):
                if a not in visited:
                    stack.push(a)

def main():
    filepath = input("Enter file path: ")
    graph = read_graph(filepath)
    while True:
        node = input("Enter node: ")
        if node in graph:
            break
        print(node, "is not a valid node")
    print()
    dfsit(graph, node)

if __name__ == "__main__":
    main()
