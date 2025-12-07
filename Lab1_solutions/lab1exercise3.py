
def read_tree(filepath):
    with open(filepath) as f:
        return read_tree_rec(f)

def read_tree_rec(f):
    node = f.readline().strip()
    if node == 'Q':
        return [ f.readline().strip() , read_tree_rec(f), read_tree_rec(f) ]
    return [ f.readline().strip() ]

def yesno(question):
    answer = input(question + '? (y/n): ').strip().lower()
    while answer != 'y' and answer != 'n':
        answer = input(question + '? (y/n): ').strip().lower()
    return answer == 'y'

def diagnose(tree):
    while len(tree) > 1:
        tree = tree[1] if yesno(tree[0]) else tree[2]
    print(tree[0])

def main():
    filepath = input('Enter file path: ')
    tree = read_tree(filepath)
    diagnose(tree)

if __name__ == '__main__':
    main()
