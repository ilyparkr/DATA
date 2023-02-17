class ArrayStack:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def is_empty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def push(self, item):
        self.data.append(item)
        return

    def pop(self):
        if self.is_empty() == True:
            print('Underflow: Cannot pop data from an empty list')
        else:
            pop_val = self.data[-1]
            self.data.pop()
            return pop_val

    def stackTop(self):
        return self.data[-1]

    def printStack(self):
        print(self.data)

def is_parenthesis_matching(str):
    stack = ArrayStack()
    for i in str:
        if i == '(':
            stack.push(i)
        elif i == ')':
            if stack.is_empty():
                print('Parentheses in ' + str + ' are unmatched')
                return False
            else:
                stack.pop()
    if stack.is_empty():
        return True
    else:
        print('Parentheses in ' + str + ' are unmatched')
        return False

print(is_parenthesis_matching("(((A-B)*C)"))
