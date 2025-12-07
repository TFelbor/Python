from stack import Stack

def checkbalance(string):
    """
    Check the balance of the string 'string'
    :param string: the string to check
    :return: -1 if the string is balanced, or the
    index of the imbalanced otherwise
    """
    stack = Stack()
    index_counter = 0
    for c in string:
        if c == '(' or c == '{' or c == '[':
            stack.push(c)
        elif c == ')' or c == '}' or c == ']' :
            if stack.is_empty():
                return index_counter
            if stack.peek() == '(' and c == ')':
                stack.pop()
            elif stack.peek() != '(' and c == ')':
                return index_counter
            if stack.peek() == '{' and c == '}':
                stack.pop()
            elif stack.peek() != '{' and c == '}':
                return index_counter
            if stack.peek() == '[' and c == ']':
                stack.pop()
            elif stack.peek() != '[' and c == ']':
                return index_counter
        index_counter += 1
    return -1


def stop():
    while True:
        answer = input("more ('y' or 'n')? ").strip().lower()
        if answer == 'y':
            return False
        elif answer == 'n':
            return True

def main():
    print("Checking balance...")
    while True:
        string = input("your string: ")
        index = checkbalance(string)
        if index > -1:
            print("the string is not balanced:\n")
            print(string)
            print(' ' * index + '^')
        else:
            print("the string is balanced:\n")
        if stop():
            break
    print("done")

if __name__ == '__main__':
    main()
