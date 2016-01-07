class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[len(self.items) - 1]
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()

def revstring(mystr):
    stack = Stack()
    newstr = ''
    for ch in mystr:
        stack.push(ch)
    while not stack.isEmpty():
        newstr += stack.pop()
    return newstr

print(revstring('hello'))