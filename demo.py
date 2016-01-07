# stack栈
# 使用栈实现字符串反序输出
from pyds.basic import Stack

def revstring(mystr):
    mystack = Stack()
    newstr = ''
    for ch in mystr:
        mystack.push(ch)
    while not mystack.is_empty():
        newstr += mystack.pop()
    return newstr

print(revstring('hello'))