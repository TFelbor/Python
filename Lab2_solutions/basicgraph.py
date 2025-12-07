import random

def read_graph(filename):
    graph = {}
    with open(filename) as f:
        for line in f:
            line = line.strip().split(':')
            graph[line[0]] = line[1].split(',')
    return graph

def adjacent(graph,node):
    if node in graph:
        return iter(graph[node])
    else:
        raise KeyError('node ' + node + ' not in graph')

def random_node(graph):
    return random.choice(list(graph))

def main():
    filepath = input('Enter file path: ')
    graph = read_graph(filepath)
    print(graph)
    v = random_node(graph)
    print('a random node:', v)
    print('the adjacent of',v,':')
    for a in adjacent(graph,v):
        print(a, end=' ')

if __name__ == '__main__':
    main()
