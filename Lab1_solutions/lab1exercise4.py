from lab1exercise3 import read_tree

def write_tree(filepath, tree):
    with open(filepath, 'w') as f:
        write_tree_rec(f, tree)

def write_tree_rec(f, tree):
    if len(tree) > 1:
        f.write(f'Q\n{tree[0]}\n')
        write_tree_rec(f, tree[1])
        write_tree_rec(f, tree[2])
    else:
        f.write(f'A\n{tree[0]}\n')

def yesno(question):
    answer = input(question + ' (y/n)?: ').strip().lower()
    while answer != 'y' and answer != 'n':
        answer = input(question + ' (y/n)?: ').strip().lower()
    return answer == 'y'

def play(tree):
    while len(tree) > 1:
        tree = tree[1] if yesno(tree[0]) else tree[2]
    check_answer(tree)

def check_answer(tree):
    if yesno(f'is your animal a {tree[0]}'):
        print("I got it, I'm a genius!!")
        return
    wrong = tree[0]
    new = input('what is your animal? ').strip()
    tree[0] = input(f'give a yes/no question to distinguish between a {wrong} and a {new}: ').strip()
    if yesno('what is the answer to that question'):
        tree.append([new])
        tree.append([wrong])
    else:
        tree.append([wrong])
        tree.append([new])

def main():
    filepath = input('enter the filepath: ')
    tree = read_tree(filepath)
    while True:
        play(tree)
        if yesno('do you want to save the tree'):
            write_tree(filepath, tree)
        if not yesno('do you want to play again'):
            break

if __name__ == '__main__':
    main()

