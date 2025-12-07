from basicgraph import read_graph, adjacent

def bfs(graph, node):
    dist = {node: 0}
    pred = {node: None}
    queue = [node]
    while queue:
        v = queue.pop(0)
        for a in adjacent(graph, v):
            if a in dist:
                continue
            dist[a] = dist[v] + 1
            pred[a] = v
            queue.append(a)
    return pred, dist

def display_path(pred, node):
    if pred[node] is None:
        print(node,end='')
        return
    display_path(pred, pred[node])
    print(',',node,end='')

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
