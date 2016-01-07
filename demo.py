from basic import Stack

def revstring(mystr):
    stack = Stack()
    newstr = ''
    for ch in mystr:
        stack.push(ch)
    while not stack.isEmpty():
        newstr += stack.pop()
    return newstr

print(revstring('hello'))