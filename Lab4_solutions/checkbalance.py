from Lab4.stack import Stack

def is_opening(char):
    return char in "({["

def is_closing(char):
    return char in ")}]"

def no_match(opening, closing):
    return "({[".index(opening) != ")}]".index(closing)

def checkbalance(string):
    """
    Check the balance of the string 'string'
    :param string: the string to check
    :return: -1 if the string is balanced, or the
    index of the imbalanced otherwise
    """
    stack = Stack()
    index = 0
    for char in string:
        if is_opening(char):
            stack.push(char)
        elif is_closing(char):
            if stack.is_empty() or no_match(stack.pop(), char):
                return index
        index += 1
    if stack.is_empty():
        return None
    return index

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
        if index:
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